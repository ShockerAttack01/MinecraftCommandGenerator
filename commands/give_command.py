"""
GiveCommand Module

This module implements the Minecraft /give command interface, providing a user-friendly way to generate
give commands with item search, category filtering, and parameter validation.

The command follows the format: /give <player> <item> [amount] [nbt]

Key Features:
- Player selection with target selectors (@a, @p, @e, @r, @s)
- Item search with category filtering
- Amount specification
- NBT data input
- Real-time command validation and feedback
- Sorted item categories and suggestions
- Version-based item filtering
"""

import customtkinter as ctk
from typing import Dict, List, Tuple, Any
from .base_command import BaseCommand
from minecraft_data import TARGET_SELECTORS, ITEM_CATEGORIES, COMMAND_TYPES, ITEM_TAGS, ITEM_VERSIONS, VERSIONS
from command_summarizer import CommandSummarizer
import re
import threading
import time

class GiveCommand(BaseCommand):
    """
    Command class for generating Minecraft /give commands.
    
    This class extends BaseCommand to provide a specialized interface for the /give command,
    including item search, category filtering, and parameter validation.
    
    Attributes:
        item_categories (Dict[str, List[str]]): Dictionary mapping category names to lists of item IDs
        all_items (List[str]): List of all available item IDs
        all_formatted_items (List[str]): List of formatted item names for display
        category_var (StringVar): Tkinter variable for the selected category
        suggestions_frame (CTkScrollableFrame): Frame containing item suggestions
        version_var (StringVar): Tkinter variable for the selected Minecraft version
        loading_thread (Thread): Thread for loading item suggestions
        is_loading (bool): Flag indicating if suggestions are being loaded
    """
    
    def __init__(self, master: ctk.CTkFrame, command_data: Dict[str, Any], all_formatted_items: List[str]):
        """
        Initialize the give command interface.
        
        Args:
            master (CTkFrame): The parent frame for the command UI
            command_data (Dict[str, Any]): Command configuration data
            all_formatted_items (List[str]): List of all available items in display format
        
        The initialization process:
        1. Collects all items from categories
        2. Adds any additional items from all_formatted_items
        3. Sorts items alphabetically
        4. Sets up the UI components
        """
        # Process all items and categories
        self.item_categories = ITEM_CATEGORIES
        
        # First collect all items from categories
        category_items = set()
        for items in self.item_categories.values():
            category_items.update(items)
        
        # Then add any additional items from all_formatted_items
        self.all_items = list(category_items)
        self.all_formatted_items = [item.replace("_", " ").title() for item in self.all_items]
        
        # Add any items from all_formatted_items that aren't in categories
        for item in all_formatted_items:
            raw_item = item.lower().replace(" ", "_")
            if raw_item not in category_items:
                self.all_items.append(raw_item)
                self.all_formatted_items.append(item)
        
        # Create item data structure with tags and versions
        self.item_data = []
        for formatted_item, raw_item in zip(self.all_formatted_items, self.all_items):
            # Get tags from ITEM_TAGS or create default tags
            tags = ITEM_TAGS.get(raw_item, set())
            if not tags:
                # Add category as a tag
                for category, items in self.item_categories.items():
                    if raw_item in items:
                        tags.add(category.lower())
                # Add words from item name as tags
                words = raw_item.split('_')
                tags.update(words)
                # Add formatted name words as tags
                formatted_words = formatted_item.lower().split()
                tags.update(formatted_words)
            
            # Get version from ITEM_VERSIONS or default to 1.0
            version = ITEM_VERSIONS.get(raw_item, "1.0")
            
            self.item_data.append({
                'formatted': formatted_item,
                'raw': raw_item,
                'tags': tags,
                'version': version
            })
        
        # Sort items alphabetically
        self.item_data.sort(key=lambda x: x['formatted'])
        
        # Initialize loading state
        self.is_loading = False
        self.loading_thread = None
        
        super().__init__(master, "give", command_data)
    
    def setup_ui(self):
        """
        Set up the UI elements for the give command.
        
        Creates and arranges the following components:
        1. Player input with target selector
        2. Version selector
        3. Item search with category selector
        4. Amount input
        5. NBT input
        6. Initial item suggestions
        """
        # Create player parameter with target selector
        player_frame = ctk.CTkFrame(self.param_frame)
        player_frame.pack(fill="x", padx=5, pady=2)
        self.create_player_input(player_frame)
        
        # Create version selector
        version_frame = ctk.CTkFrame(self.param_frame)
        version_frame.pack(fill="x", padx=5, pady=2)
        self.create_version_selector(version_frame)
        
        # Create item parameter with search box and category selector
        item_frame = ctk.CTkFrame(self.param_frame)
        item_frame.pack(fill="x", padx=5, pady=2)
        self.create_item_search(item_frame)
        
        # Create amount parameter
        amount_frame = ctk.CTkFrame(self.param_frame)
        amount_frame.pack(fill="x", padx=5, pady=2)
        self.create_amount_input(amount_frame)
        
        # Create NBT parameter
        nbt_frame = ctk.CTkFrame(self.param_frame)
        nbt_frame.pack(fill="x", padx=5, pady=2)
        self.create_nbt_input(nbt_frame)
        
        # Show initial suggestions
        self.update_suggestions()
    
    def create_player_input(self, frame: ctk.CTkFrame):
        """
        Create the player input section with target selector.
        
        Args:
            frame (CTkFrame): The parent frame for the player input
        
        Components:
        - Label: "Player:"
        - Entry field: For manual player name input
        - Dropdown: For target selector selection (@a, @p, @e, @r, @s)
        """
        # Add label
        label = ctk.CTkLabel(frame, text="Player:")
        label.pack(side="left", padx=5)
        
        # Create entry field
        entry = ctk.CTkEntry(frame)
        entry.pack(side="left", fill="x", expand=True, padx=5)
        
        # Create dropdown for target selectors
        selector_var = ctk.StringVar()
        dropdown = ctk.CTkOptionMenu(
            frame,
            values=TARGET_SELECTORS,
            variable=selector_var,
            command=lambda value: self.on_selector_selected("player", value)
        )
        dropdown.pack(side="left", padx=5)
        
        # Store the widgets
        self.parameter_vars["player"] = {
            "selector": selector_var,
            "entry": entry
        }
        
        # Bind events to update feedback
        entry.bind("<KeyRelease>", lambda e: self.on_parameter_change(e))
        entry.bind("<FocusOut>", lambda e: self.on_parameter_change(e))
        
        # Initialize feedback
        self.on_parameter_change(None)
    
    def create_version_selector(self, frame: ctk.CTkFrame):
        """
        Create the version selector dropdown.
        
        Args:
            frame (CTkFrame): The parent frame for the version selector
        
        Components:
        - Label: "Version:"
        - Dropdown: For selecting Minecraft version
        """
        # Add label
        label = ctk.CTkLabel(frame, text="Version:")
        label.pack(side="left", padx=5)
        
        # Create version selector
        self.version_var = ctk.StringVar(value=VERSIONS[0])  # Default to latest version
        version_dropdown = ctk.CTkOptionMenu(
            frame,
            values=VERSIONS,
            variable=self.version_var,
            command=self.on_version_change
        )
        version_dropdown.pack(side="left", padx=5)
    
    def on_version_change(self, version: str):
        """
        Handle version selection change.
        
        Args:
            version (str): The newly selected version
        
        Process:
        1. Updates suggestions based on selected version
        2. Triggers command update
        """
        self.update_suggestions()
        self.on_parameter_change()
    
    def create_item_search(self, frame: ctk.CTkFrame):
        """
        Create the item search interface with category selector.
        
        Args:
            frame (CTkFrame): The parent frame for the item search
        
        Components:
        - Label: "Item:"
        - Category dropdown: For filtering items by category
        - Search entry: For searching items
        - Suggestions frame: Scrollable frame showing matching items
        """
        # Create a frame for the search box and category selector
        search_frame = ctk.CTkFrame(frame)
        search_frame.pack(fill="x", padx=5, pady=2)
        
        # Add label
        label = ctk.CTkLabel(search_frame, text="Item:")
        label.pack(side="left", padx=5)
        
        # Create category selector
        self.category_var = ctk.StringVar(value="All Categories")
        categories = ["All Categories"] + sorted(self.item_categories.keys())
        category_dropdown = ctk.CTkOptionMenu(
            search_frame,
            values=categories,
            variable=self.category_var,
            command=self.on_category_change
        )
        category_dropdown.pack(side="left", padx=5)
        
        # Create entry field
        entry = ctk.CTkEntry(search_frame)
        entry.pack(side="left", fill="x", expand=True, padx=5)
        entry.bind("<KeyRelease>", self.on_item_search)
        
        # Create suggestions frame with scrollbar
        self.suggestions_frame = ctk.CTkScrollableFrame(frame, height=150)
        self.suggestions_frame.pack(fill="x", padx=5, pady=2)
        
        # Store the entry widget
        self.parameter_vars["item"] = entry
    
    def create_amount_input(self, frame: ctk.CTkFrame):
        """
        Create the amount input field.
        
        Args:
            frame (CTkFrame): The parent frame for the amount input
        
        Components:
        - Label: "Amount:"
        - Entry field: For specifying item quantity (defaults to 1)
        """
        # Add label
        label = ctk.CTkLabel(frame, text="Amount:")
        label.pack(side="left", padx=5)
        
        # Create entry field
        entry = ctk.CTkEntry(frame)
        entry.pack(side="left", fill="x", expand=True, padx=5)
        entry.insert(0, "1")  # Default amount
        
        # Store the entry widget
        self.parameter_vars["amount"] = entry
        
        # Bind events to update feedback
        entry.bind("<KeyRelease>", lambda e: self.on_parameter_change(e))
        entry.bind("<FocusOut>", lambda e: self.on_parameter_change(e))
        
        # Initialize feedback
        self.on_parameter_change(None)
    
    def create_nbt_input(self, frame: ctk.CTkFrame):
        """
        Create the NBT input field.
        
        Args:
            frame (CTkFrame): The parent frame for the NBT input
        
        Components:
        - Label: "NBT:"
        - Entry field: For specifying NBT data
        """
        # Add label
        label = ctk.CTkLabel(frame, text="NBT:")
        label.pack(side="left", padx=5)
        
        # Create entry field
        entry = ctk.CTkEntry(frame)
        entry.pack(side="left", fill="x", expand=True, padx=5)
        
        # Store the entry widget
        self.parameter_vars["nbt"] = entry
        
        # Bind events to update feedback
        entry.bind("<KeyRelease>", lambda e: self.on_parameter_change(e))
        entry.bind("<FocusOut>", lambda e: self.on_parameter_change(e))
        
        # Initialize feedback
        self.on_parameter_change(None)
    
    def update_suggestions(self, search_text: str = ""):
        """
        Update the item suggestions based on search text, selected category, and version.
        
        Args:
            search_text (str): The text to filter items by (default: "")
        
        Process:
        1. Clears existing suggestions
        2. Gets items based on selected category and version
        3. Filters items based on search text and tags
        4. Creates buttons for matching items
        """
        # Clear previous suggestions
        for widget in self.suggestions_frame.winfo_children():
            widget.destroy()
        
        selected_category = self.category_var.get()
        selected_version = self.version_var.get()
        search_text = search_text.lower()
        
        # Start loading in background thread
        if self.loading_thread and self.loading_thread.is_alive():
            self.is_loading = False
            self.loading_thread.join()
        
        self.is_loading = True
        self.loading_thread = threading.Thread(
            target=self._load_suggestions,
            args=(selected_category, selected_version, search_text)
        )
        self.loading_thread.start()
    
    def _load_suggestions(self, category: str, version: str, search_text: str):
        """
        Load suggestions in a background thread.
        
        Args:
            category (str): Selected category
            version (str): Selected version
            search_text (str): Search text
        """
        # Filter items based on category, version, and search
        matches = []
        for item in self.item_data:
            # Check category filter
            if category != "All Categories":
                if item['raw'] not in self.item_categories[category]:
                    continue
            
            # Check version filter
            if self._compare_versions(item['version'], version) > 0:
                continue
            
            # Check search text
            if not search_text:
                matches.append(item)
            else:
                # Check if search text matches any tag
                if any(search_text in tag for tag in item['tags']):
                    matches.append(item)
                # Also check if it matches the formatted or raw name
                elif search_text in item['formatted'].lower() or search_text in item['raw']:
                    matches.append(item)
            
            # Add a small delay to prevent UI freezing
            if len(matches) % 10 == 0:
                time.sleep(0.001)
                if not self.is_loading:
                    return
        
        # Sort matches by tag priority
        if search_text:
            matches.sort(key=lambda x: (
                # First priority: exact tag match
                not any(search_text == tag for tag in x['tags']),
                # Second priority: tag contains search text
                not any(search_text in tag for tag in x['tags']),
                # Third priority: formatted name contains search text
                search_text not in x['formatted'].lower(),
                # Fourth priority: raw name contains search text
                search_text not in x['raw'],
                # Finally sort alphabetically
                x['formatted']
            ))
        
        # Create buttons in the main thread
        self.master.after(0, self._create_suggestion_buttons, matches)
    
    def _create_suggestion_buttons(self, matches: List[Dict[str, Any]]):
        """
        Create suggestion buttons in the main thread.
        
        Args:
            matches (List[Dict[str, Any]]): List of matching items
        """
        if not self.is_loading:
            return
            
        for item in matches:
            if not self.is_loading:
                return
                
            btn = ctk.CTkButton(
                self.suggestions_frame,
                text=f"{item['formatted']} ({item['version']})",
                command=lambda f=item['formatted'], r=item['raw']: self.on_item_selected(f, r)
            )
            btn.pack(fill="x", padx=5, pady=1)
            
            # Add a small delay to prevent UI freezing
            if len(self.suggestions_frame.winfo_children()) % 10 == 0:
                time.sleep(0.001)
    
    def _compare_versions(self, version1: str, version2: str) -> int:
        """
        Compare two version strings.
        
        Args:
            version1 (str): First version string
            version2 (str): Second version string
            
        Returns:
            int: 1 if version1 > version2, -1 if version1 < version2, 0 if equal
        """
        v1_parts = [int(x) for x in version1.split('.')]
        v2_parts = [int(x) for x in version2.split('.')]
        
        for i in range(max(len(v1_parts), len(v2_parts))):
            v1 = v1_parts[i] if i < len(v1_parts) else 0
            v2 = v2_parts[i] if i < len(v2_parts) else 0
            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        return 0
    
    def on_category_change(self, category: str):
        """
        Handle category selection change.
        
        Args:
            category (str): The newly selected category
        
        Process:
        1. Clears current item selection
        2. Updates suggestions for the new category
        3. Triggers command update
        """
        # Clear current item selection
        self.parameter_vars["item"].delete(0, "end")
        if "raw_item" in self.parameter_vars:
            del self.parameter_vars["raw_item"]
        
        # Update suggestions
        self.update_suggestions()
        self.on_parameter_change()
    
    def on_item_search(self, event):
        """
        Handle item search input.
        
        Args:
            event: The key release event
        
        Process:
        1. Gets current search text
        2. Updates suggestions based on search
        3. Triggers command update
        """
        search_text = self.parameter_vars["item"].get().lower()
        self.update_suggestions(search_text)
        self.on_parameter_change()
    
    def on_item_selected(self, formatted_item: str, raw_item: str):
        """
        Handle item selection from suggestions.
        
        Args:
            formatted_item (str): The formatted display name of the selected item
            raw_item (str): The raw item ID for command generation
        
        Process:
        1. Updates search box with selected item
        2. Stores raw item ID for command generation
        3. Updates suggestions
        4. Triggers command update
        """
        self.parameter_vars["item"].delete(0, "end")
        self.parameter_vars["item"].insert(0, formatted_item)
        
        # Store the raw item ID for command generation
        self.parameter_vars["raw_item"] = raw_item
        
        # Update suggestions to show all items again
        self.update_suggestions()
        
        self.on_parameter_change()
    
    def update_command(self):
        """
        Update the command output based on current parameter values.
        
        Returns:
            str: The generated command string
        
        Format: /give <player> <item> [amount] [nbt]
        """
        command_parts = [self.command_type]
        
        # Add player parameter
        player = self.get_parameter_value("player")
        if player:
            command_parts.append(player)
        
        # Add item parameter
        if "raw_item" in self.parameter_vars:
            command_parts.append(self.parameter_vars["raw_item"])
        else:
            item = self.get_parameter_value("item")
            if item:
                command_parts.append(item.lower().replace(" ", "_"))
        
        # Add amount parameter
        amount = self.get_parameter_value("amount")
        if amount and amount != "1":
            command_parts.append(amount)
        
        # Add NBT parameter
        nbt = self.get_parameter_value("nbt")
        if nbt:
            command_parts.append(nbt)
        
        return " ".join(command_parts)
        
    def get_feedback(self) -> List[str]:
        """
        Get feedback about the current command state.
        
        Returns:
            List[str]: List of feedback messages
        
        Feedback includes:
        - Command description
        - Parameter validation
        - Item category information
        - Command validity status
        """
        feedback = []
        command_parts = self.update_command().split()
        
        # Basic validation
        if len(command_parts) < 3:
            feedback.append("⚠️ Command is incomplete. Please fill in player and item.")
            return feedback
            
        # Add command summary using CommandSummarizer
        params = {
            "player": self.get_parameter_value("player"),
            "item": self.get_parameter_value("item"),
            "amount": self.get_parameter_value("amount")
        }
        feedback.append(CommandSummarizer.summarize("give", params))
        feedback.append("")
        
        # Player validation
        player = command_parts[1]
        if not (player in TARGET_SELECTORS or re.match(r"^[a-zA-Z0-9_]{1,16}$", player)):
            feedback.append("⚠️ Invalid player/target selector. Must be a valid player name or target selector (@a, @p, @e, @r, @s).")
            
        # Item validation
        item_id = command_parts[2]
        if not re.match(r"^[a-z0-9_]+$", item_id):
            feedback.append("⚠️ Invalid item ID. Must be lowercase letters, numbers, and underscores only.")
            
        # Amount validation
        if len(command_parts) > 3 and not command_parts[3].isdigit():
            feedback.append("⚠️ Amount must be a number.")
            
        # Find item in categories and show formatted name
        item_found = False
        for category, items in self.item_categories.items():
            if item_id in items:
                item_found = True
                formatted_name = item_id.replace("_", " ").title()
                amount = command_parts[3] if len(command_parts) > 3 else "1"
                feedback.append(f"🎁 You will receive: {amount}x {formatted_name}")
                feedback.append(f"📦 Category: {category}")
                break
                
        if not item_found and item_id:
            feedback.append("⚠️ Unknown item ID. Please select an item from the search box.")
            
        if not feedback or (len(feedback) == 1 and feedback[0].startswith("📝")):
            feedback.append("✅ Command looks valid!")
            feedback.append("")
            feedback.append("Parameters:")
            for param in self.command_data["parameters"]:
                if param in self.command_data["feedback"]:
                    feedback.append(f"• {param}: {self.command_data['feedback'][param]}")
                    
        return feedback

    def on_parameter_change(self, event=None):
        """Handle changes to parameter values."""
        # Update command and feedback
        self.update_command()
        if hasattr(self.master, "master") and hasattr(self.master.master, "update_command"):
            self.master.master.update_command() 