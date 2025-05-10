"""
GiveCommand Module

This module implements the Minecraft /give command interface, providing a user-friendly way to generate
give commands with item search, category filtering, and parameter validation.

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
from typing import Dict, List, Any
from .base_command import BaseCommand
from data.minecraft_data import TARGET_SELECTORS, ITEM_CATEGORIES, ITEM_TAGS, ITEM_VERSIONS, VERSIONS, ENCHANTMENTS, ATTRIBUTES
from command_summarizer import CommandSummarizer
import re
import threading
import time

class GiveCommand(BaseCommand):
    """
    Command class for generating Minecraft /give commands.
    
    This class extends BaseCommand to provide a specialized interface for the /give command,
    including item search, category filtering, and parameter validation.
    """

    def __init__(self, master: ctk.CTkFrame, command_data: Dict[str, Any], all_formatted_items: List[str], version_var: ctk.StringVar):
        """
        Initialize the give command interface.

        Args:
            master (CTkFrame): The parent frame for the command UI.
            command_data (Dict[str, Any]): Command configuration data.
            all_formatted_items (List[str]): List of all available items in display format.
            version_var (StringVar): The version variable from the parent frame.
        """
        # Process all items and categories
        self.version_var = version_var
        self.item_categories = ITEM_CATEGORIES
        category_items = set(item for items in self.item_categories.values() for item in items)

        # Add additional items from all_formatted_items
        self.all_items = list(category_items)
        self.all_formatted_items = [item.replace("_", " ").title() for item in self.all_items]
        for item in all_formatted_items:
            raw_item = item.lower().replace(" ", "_")
            if raw_item not in category_items:
                self.all_items.append(raw_item)
                self.all_formatted_items.append(item)

        # Create item data structure with tags and versions
        self.item_data = [
            {
                'formatted': formatted_item,
                'raw': raw_item,
                'tags': ITEM_TAGS.get(raw_item, set()) | set(raw_item.split('_')) | set(formatted_item.lower().split()),
                'version': ITEM_VERSIONS.get(raw_item, "1.0")
            }
            for formatted_item, raw_item in zip(self.all_formatted_items, self.all_items)
        ]
        self.item_data.sort(key=lambda x: x['formatted'])

        # Initialize loading state
        self.is_loading = False
        self.loading_thread = None

        super().__init__(master, "give", command_data)

    def setup_ui(self) -> None:
        """
        Set up the UI elements for the give command.

        Creates and arranges the following components:
        1. Player input with target selector
        2. Item search with category selector
        3. Amount input
        4. NBT input with structured interface
        """
        # Create player parameter with target selector
        player_frame = ctk.CTkFrame(self.param_frame)
        player_frame.pack(fill="x", padx=5, pady=2)
        self.create_player_input(player_frame)

        # Create item parameter with search box and category selector
        item_frame = ctk.CTkFrame(self.param_frame)
        item_frame.pack(fill="x", padx=5, pady=2)
        self.create_item_search(item_frame)

        # Create amount parameter
        amount_frame = ctk.CTkFrame(self.param_frame)
        amount_frame.pack(fill="x", padx=5, pady=2)
        self.create_amount_input(amount_frame)

        # Create NBT parameter with structured input
        nbt_frame = ctk.CTkFrame(self.param_frame)
        nbt_frame.pack(fill="x", padx=5, pady=2)
        self.create_nbt_input(nbt_frame)

        # Show initial suggestions
        self.update_suggestions()
    
    def create_player_input(self, frame: ctk.CTkFrame) -> None:
        """
        Create the player input section with target selector.
        
        Args:
            frame (CTkFrame): The parent frame for the player input.
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
    
    def create_version_selector(self, frame: ctk.CTkFrame) -> None:
        """
        Create the version selector dropdown.
        
        Args:
            frame (CTkFrame): The parent frame for the version selector.
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
    
    def on_version_change(self, version: str) -> None:
        """
        Handle version selection change.
        
        Args:
            version (str): The newly selected version.
        """
        self.version_var.set(version)
        self.update_suggestions()  # Reload suggestions based on the new version
        self.on_parameter_change()
    
    def create_item_search(self, frame: ctk.CTkFrame) -> None:
        """
        Create the item search interface with category selector.
        
        Args:
            frame (CTkFrame): The parent frame for the item search.
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
    
    def create_amount_input(self, frame: ctk.CTkFrame) -> None:
        """
        Create the amount input field.
        
        Args:
            frame (CTkFrame): The parent frame for the amount input.
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
    
    def create_nbt_input(self, frame: ctk.CTkFrame) -> None:
        """
        Create the NBT input field with multiple buttons for predefined NBT data options.

        Args:
            frame (CTkFrame): The parent frame for the NBT input.
        """
        # Add label
        label = ctk.CTkLabel(frame, text="NBT Data:")
        label.pack(side="top", anchor="w", padx=5)

        # Create entry field for raw NBT input
        entry = ctk.CTkEntry(frame)
        entry.pack(fill="x", padx=5, pady=2)
        entry.bind("<KeyRelease>", self.on_nbt_change)

        # Store the entry widget
        self.parameter_vars["nbt"] = entry

        # Create a frame for NBT option buttons
        nbt_buttons_frame = ctk.CTkFrame(frame)
        nbt_buttons_frame.pack(fill="x", padx=5, pady=5)

        # Create a frame for the helper line (hidden by default)
        self.nbt_helper_frame = ctk.CTkFrame(frame)
        self.nbt_helper_frame.pack(fill="x", padx=5, pady=5)
        self.nbt_helper_frame.pack_forget()  # Hide initially

        # Define predefined NBT options with helper callbacks
        nbt_options = {
            "Custom Name": self.show_custom_name_helper,
            "Lore": self.show_lore_helper,
            "Enchantments": self.show_enchantments_helper,
            "Attributes": self.show_attributes_helper,
            "Unbreakable": lambda: self.append_nbt_data('{"Unbreakable":1b}')
        }

        # Create buttons for each NBT option
        for label, command in nbt_options.items():
            button = ctk.CTkButton(
                nbt_buttons_frame,
                text=label,
                command=command,
                height=30
            )
            button.pack(side="left", padx=5, pady=2)

    def show_custom_name_helper(self) -> None:
        """
        Show a helper line for adding a custom name.
        """
        self.clear_nbt_helper_frame()
        label = ctk.CTkLabel(self.nbt_helper_frame, text="Enter Custom Name:")
        label.pack(side="left", padx=5)
        entry = ctk.CTkEntry(self.nbt_helper_frame)
        entry.pack(side="left", fill="x", expand=True, padx=5)
        apply_button = ctk.CTkButton(
            self.nbt_helper_frame,
            text="Apply",
            command=lambda: self.apply_custom_name(entry.get())
        )
        apply_button.pack(side="left", padx=5)
        self.nbt_helper_frame.pack(fill="x", padx=5, pady=5)

    def apply_custom_name(self, name: str) -> None:
        """
        Apply the custom name to the NBT data.

        Args:
            name (str): The custom name to apply.
        """
        if name:
            self.append_nbt_data(f'{{"display":{{"Name":"{{\\"text\\":\\"{name}\\"}}"}}}}')
        self.nbt_helper_frame.pack_forget()

    def show_lore_helper(self) -> None:
        """
        Show a helper line for adding lore.
        """
        self.clear_nbt_helper_frame()
        label = ctk.CTkLabel(self.nbt_helper_frame, text="Enter Lore (comma-separated):")
        label.pack(side="left", padx=5)
        entry = ctk.CTkEntry(self.nbt_helper_frame)
        entry.pack(side="left", fill="x", expand=True, padx=5)
        apply_button = ctk.CTkButton(
            self.nbt_helper_frame,
            text="Apply",
            command=lambda: self.apply_lore(entry.get())
        )
        apply_button.pack(side="left", padx=5)
        self.nbt_helper_frame.pack(fill="x", padx=5, pady=5)

    def apply_lore(self, lore: str) -> None:
        """
        Apply the lore to the NBT data.

        Args:
            lore (str): The lore to apply (comma-separated).
        """
        if lore:
            lore_lines = lore.split(",")
            lore_json = ','.join([f'{{"text":"{line.strip()}"}}' for line in lore_lines])
            self.append_nbt_data(f'{{"display":{{"Lore":[{lore_json}]}}}}')
        self.nbt_helper_frame.pack_forget()

    def show_enchantments_helper(self) -> None:
        """
        Show a helper line for adding enchantments.
        """
        self.clear_nbt_helper_frame()
        label = ctk.CTkLabel(self.nbt_helper_frame, text="Select Enchantment:")
        label.pack(side="left", padx=5)
        enchantment_var = ctk.StringVar(value=ENCHANTMENTS[0])
        dropdown = ctk.CTkOptionMenu(self.nbt_helper_frame, values=ENCHANTMENTS, variable=enchantment_var)
        dropdown.pack(side="left", padx=5)
        level_label = ctk.CTkLabel(self.nbt_helper_frame, text="Level:")
        level_label.pack(side="left", padx=5)
        level_entry = ctk.CTkEntry(self.nbt_helper_frame, width=50)
        level_entry.pack(side="left", padx=5)
        apply_button = ctk.CTkButton(
            self.nbt_helper_frame,
            text="Apply",
            command=lambda: self.apply_enchantments(enchantment_var.get(), level_entry.get())
        )
        apply_button.pack(side="left", padx=5)
        self.nbt_helper_frame.pack(fill="x", padx=5, pady=5)

    def apply_enchantments(self, enchantment: str, level: str) -> None:
        """
        Apply the enchantments to the NBT data.

        Args:
            enchantment (str): The enchantment ID.
            level (str): The enchantment level.
        """
        if enchantment and level.isdigit():
            self.append_nbt_data(f'{{"Enchantments":[{{"id":"minecraft:{enchantment}","lvl":{level}s}}]}}')
        self.nbt_helper_frame.pack_forget()

    def show_attributes_helper(self) -> None:
        """
        Show a helper line for adding attributes.
        """
        self.clear_nbt_helper_frame()
        label = ctk.CTkLabel(self.nbt_helper_frame, text="Select Attribute:")
        label.pack(side="left", padx=5)
        attribute_var = ctk.StringVar(value=ATTRIBUTES[0])
        dropdown = ctk.CTkOptionMenu(self.nbt_helper_frame, values=ATTRIBUTES, variable=attribute_var)
        dropdown.pack(side="left", padx=5)
        amount_label = ctk.CTkLabel(self.nbt_helper_frame, text="Amount:")
        amount_label.pack(side="left", padx=5)
        amount_entry = ctk.CTkEntry(self.nbt_helper_frame, width=50)
        amount_entry.pack(side="left", padx=5)
        apply_button = ctk.CTkButton(
            self.nbt_helper_frame,
            text="Apply",
            command=lambda: self.apply_attributes(attribute_var.get(), amount_entry.get())
        )
        apply_button.pack(side="left", padx=5)
        self.nbt_helper_frame.pack(fill="x", padx=5, pady=5)

    def apply_attributes(self, attribute: str, amount: str) -> None:
        """
        Apply the attributes to the NBT data.

        Args:
            attribute (str): The attribute name.
            amount (str): The attribute amount.
        """
        if attribute and amount.isdigit():
            self.append_nbt_data(
                f'{{"AttributeModifiers":[{{"AttributeName":"{attribute}","Name":"{attribute}","Amount":{amount},"Operation":0,"UUID":[I;1,2,3,4]}}]}}'
            )
        self.nbt_helper_frame.pack_forget()

    def clear_nbt_helper_frame(self) -> None:
        """
        Clear all widgets from the NBT helper frame.
        """
        for widget in self.nbt_helper_frame.winfo_children():
            widget.destroy()

    def append_nbt_data(self, nbt_data: str) -> None:
        """
        Append the selected NBT data to the existing NBT input field.

        Args:
            nbt_data (str): The NBT data to append.
        """
        current_nbt = self.parameter_vars["nbt"].get().strip()
        if current_nbt:
            # Merge the new NBT data with the existing data
            if current_nbt.endswith("}") and nbt_data.startswith("{"):
                combined_nbt = f"{current_nbt[:-1]},{nbt_data[1:]}"
            else:
                combined_nbt = f"{current_nbt},{nbt_data}"
        else:
            combined_nbt = nbt_data

        # Update the NBT input field
        self.parameter_vars["nbt"].delete(0, "end")
        self.parameter_vars["nbt"].insert(0, combined_nbt)
        self.on_parameter_change()

    def on_nbt_change(self, event) -> None:
        """
        Handle changes to the NBT input field.

        Args:
            event: The key release event.
        """
        self.on_parameter_change(event)

    def update_suggestions(self, search_text: str = "") -> None:
        """
        Update the item suggestions based on search text, selected category, and version.
        
        Args:
            search_text (str): The text to filter items by (default: "").
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
    
    def _load_suggestions(self, category: str, version: str, search_text: str) -> None:
        """
        Load suggestions in a background thread.
        
        Args:
            category (str): Selected category.
            version (str): Selected version.
            search_text (str): Search text.
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
    
    def _create_suggestion_buttons(self, matches: List[Dict[str, Any]]) -> None:
        """
        Create suggestion buttons in the main thread.
        
        Args:
            matches (List[Dict[str, Any]]): List of matching items.
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
            version1 (str): First version string.
            version2 (str): Second version string.
            
        Returns:
            int: 1 if version1 > version2, -1 if version1 < version2, 0 if equal.
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
    
    def on_category_change(self, category: str) -> None:
        """
        Handle category selection change.
        
        Args:
            category (str): The newly selected category.
        """
        # Clear current item selection
        self.parameter_vars["item"].delete(0, "end")
        if "raw_item" in self.parameter_vars:
            del self.parameter_vars["raw_item"]
        
        # Update suggestions
        self.update_suggestions()
        self.on_parameter_change()
    
    def on_item_search(self, event) -> None:
        """
        Handle item search input.
        
        Args:
            event: The key release event.
        """
        search_text = self.parameter_vars["item"].get().lower()
        self.update_suggestions(search_text)
        self.on_parameter_change()
    
    def on_item_selected(self, formatted_item: str, raw_item: str) -> None:
        """
        Handle item selection from suggestions.
        
        Args:
            formatted_item (str): The formatted display name of the selected item.
            raw_item (str): The raw item ID for command generation.
        """
        self.parameter_vars["item"].delete(0, "end")
        self.parameter_vars["item"].insert(0, formatted_item)
        
        # Store the raw item ID for command generation
        self.parameter_vars["raw_item"] = raw_item
        
        # Update suggestions to show all items again
        self.update_suggestions()
        
        self.on_parameter_change()
    
    def update_command(self) -> str:
        """
        Update the command output based on current parameter values.
        
        Returns:
            str: The generated command string.
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
            List[str]: List of feedback messages.
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

    def on_parameter_change(self, event=None) -> None:
        """Handle changes to parameter values."""
        # Update command and feedback
        self.update_command()
        if hasattr(self.master, "master") and hasattr(self.master.master, "update_command"):
            self.master.master.update_command() 


