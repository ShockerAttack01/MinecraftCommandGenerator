import customtkinter as ctk
from typing import List, Optional
from data.minecraft_data import VERSIONS, EFFECT_CATEGORIES, ITEM_CATEGORIES, COMMAND_TYPES
from commands import GiveCommand, EffectCommand, GamemodeCommand, TeleportCommand
from functools import partial
import json
import os

class SearchBox(ctk.CTkFrame):
    """
    A custom search box widget with suggestions.
    This widget allows users to type in a search field and see a list of suggestions
    based on their input. It supports filtering and selecting items from the list.
    """
    def __init__(self, master: ctk.CTkFrame, items: List[str], command: Optional[callable] = None):
        """
        Initialize the search box.

        Args:
            master (CTkFrame): The parent frame where the search box will be placed.
            items (List[str]): List of items to display as suggestions.
            command (callable, optional): Callback function triggered when an item is selected.
        """
        super().__init__(master)
        self.items = items
        self.command = command
        
        # Create entry field for user input
        self.entry = ctk.CTkEntry(self)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<KeyRelease>", self.on_key_release)  # Update suggestions on key release
        self.entry.bind("<FocusIn>", self.on_focus_in)        # Show suggestions on focus
        self.entry.bind("<FocusOut>", self.on_focus_out)      # Hide suggestions on focus out
        
        # Create a frame to hold suggestions
        self.suggestions_frame = ctk.CTkFrame(self)
        self.suggestions_frame.pack(side="left", fill="x", expand=True)
        
        # Create a scrollable frame for suggestions
        self.scrollable_frame = ctk.CTkScrollableFrame(self.suggestions_frame)
        self.scrollable_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Initialize suggestion buttons
        self.suggestion_buttons = []
        self.update_suggestions(self.items)
        
    def on_key_release(self, event):
        """
        Handle key release events in the entry field.
        Filters the suggestions based on the current input.

        Args:
            event: The key release event.
        """
        text = self.entry.get().lower()
        if not text:
            self.update_suggestions(self.items)
        else:
            filtered_items = [item for item in self.items if text in item.lower()]
            self.update_suggestions(filtered_items)
            
        if self.command:
            self.command(self.entry.get())
            
    def on_focus_in(self, event):
        """
        Handle focus-in events for the entry field.
        Displays the full list of suggestions.

        Args:
            event: The focus-in event.
        """
        self.update_suggestions(self.items)
        
    def on_focus_out(self, event):
        """
        Handle focus-out events for the entry field.
        Hides the suggestions frame.

        Args:
            event: The focus-out event.
        """
        self.suggestions_frame.pack_forget()
        
    def update_suggestions(self, items: List[str]) -> None:
        """
        Update the list of suggestions displayed in the suggestions frame.

        Args:
            items (List[str]): List of items to display as suggestions.
        """
        # Clear existing buttons
        for button in self.suggestion_buttons:
            button.destroy()
        self.suggestion_buttons.clear()
        
        # Create new buttons for each suggestion
        for item in items:
            button = ctk.CTkButton(
                self.scrollable_frame,
                text=item,
                command=lambda i=item: self.select_item(i),
                height=30
            )
            button.pack(fill="x", pady=2)
            self.suggestion_buttons.append(button)
            
        # Show or hide the suggestions frame based on the number of items
        if items:
            self.suggestions_frame.pack(side="left", fill="x", expand=True)
        else:
            self.suggestions_frame.pack_forget()
            
    def select_item(self, item: str):
        """
        Handle the selection of a suggestion.

        Args:
            item (str): The selected item.
        """
        self.entry.delete(0, "end")
        self.entry.insert(0, item)
        self.update_suggestions(self.items)
        if self.command:
            self.command(item)
            
    def get(self) -> str:
        """
        Get the current value of the entry field.

        Returns:
            str: The current value of the entry field.
        """
        return self.entry.get()
        
    def set_items(self, items: List[str]):
        """
        Update the list of items used for suggestions.

        Args:
            items (List[str]): The new list of items.
        """
        self.items = items
        self.update_suggestions(items)

class MinecraftCommandGenerator(ctk.CTk):
    """
    Main application class for the Minecraft Command Generator.
    This class creates the GUI for generating Minecraft commands and provides
    functionality for selecting command types, versions, and parameters.
    """
    FAVORITES_FILE = "data/favorites.json"  # File to store favorites

    def __init__(self):
        """
        Initialize the application.
        """
        super().__init__()
        
        self.title("Minecraft Command Generator")
        self.geometry("1200x800")  # Set the window size
        
        # Create the main frame to hold all widgets
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Create a dictionary to store favorite commands
        self.favorite_commands = set()

        # Ensure the directory for the favorites file exists
        os.makedirs(os.path.dirname(self.FAVORITES_FILE), exist_ok=True)

        # Load favorites from file
        self.favorite_commands = self.load_favorites()

        # Update the top bar layout
        self.top_bar = ctk.CTkFrame(self.main_frame, height=40)
        self.top_bar.pack(fill="x", padx=5, pady=5)

        self.home_button = ctk.CTkButton(
            self.top_bar, text="Home", width=80, height=30, command=self.show_home_page
        )
        self.home_button.pack(side="left", padx=5)

        # Create a horizontally scrollable frame for command buttons
        self.command_slider_frame = ctk.CTkScrollableFrame(
            self.top_bar, height=40, orientation="horizontal"
        )
        self.command_slider_frame.pack(side="left", fill="x", expand=True, padx=5)

        # Bind mouse wheel events for horizontal scrolling
        self.command_slider_frame._parent_canvas.bind("<Enter>", self.bind_horizontal_scroll)
        self.command_slider_frame._parent_canvas.bind("<Leave>", self.unbind_horizontal_scroll)

        # Add command buttons to the slider
        self.add_command_buttons()

        self.settings_button = ctk.CTkButton(
            self.top_bar, text="⚙️ Settings", width=80, height=30, command=self.open_settings
        )
        self.settings_button.pack(side="right", padx=5)

        # Add command buttons to the slider
        self.add_command_buttons()

        # Create the command type selector
        self.command_type_frame = ctk.CTkFrame(self.main_frame)
        self.command_type_frame.pack(fill="x", padx=5, pady=5)
        
        self.command_type_label = ctk.CTkLabel(self.command_type_frame, text="Command Type:")
        self.command_type_label.pack(side="left", padx=5)
        
        self.command_type_var = ctk.StringVar(value="")
        self.command_type_dropdown = ctk.CTkOptionMenu(
            self.command_type_frame,
            values=[""] + list(COMMAND_TYPES.keys()),
            variable=self.command_type_var,
            command=self.on_command_change
        )
        self.command_type_dropdown.pack(side="left", padx=5)

        # Bind the command type variable to actively update the UI
        self.command_type_var.trace_add("write", self.on_command_type_change)

        # Create the version selector
        self.version_frame = ctk.CTkFrame(self.main_frame)
        self.version_frame.pack(fill="x", padx=5, pady=5)
        
        self.version_label = ctk.CTkLabel(self.version_frame, text="Minecraft Version:")
        self.version_label.pack(side="left", padx=5)
        
        self.version_var = ctk.StringVar(value=VERSIONS[0])
        self.version_var.trace_add("write", self.on_version_change)
        self.version_dropdown = ctk.CTkOptionMenu(
            self.version_frame,
            values=VERSIONS,
            variable=self.version_var,
            command=self.on_version_change
        )
        self.version_dropdown.pack(side="left", padx=5)

        # Create the parameters frame for command-specific inputs
        self.parameters_frame = ctk.CTkFrame(self.main_frame)
        self.parameters_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Create the command output frame
        self.command_frame = ctk.CTkFrame(self.main_frame)
        self.command_frame.pack(fill="x", padx=5, pady=5)

        self.command_label = ctk.CTkLabel(self.command_frame, text="Command:")
        self.command_label.pack(side="left", padx=5)

        self.command_text = ctk.CTkTextbox(self.command_frame, height=50)
        self.command_text.pack(side="left", fill="x", expand=True, padx=5)

        # Create the feedback frame for additional information
        self.feedback_frame = ctk.CTkFrame(self.main_frame)
        self.feedback_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.feedback_label = ctk.CTkLabel(self.feedback_frame, text="Feedback:")
        self.feedback_label.pack(side="left", padx=5)

        self.feedback_text = ctk.CTkTextbox(self.feedback_frame, height=50)  # Increased height
        self.feedback_text.pack(side="left", fill="both", expand=True, padx=5)

        # Show the home page initially
        self.show_home_page()

        # Initialize the current command instance
        self.current_command = None

        # Preload all items and effects for suggestions
        self.all_items = []
        for category_items in ITEM_CATEGORIES.values():
            self.all_items.extend(category_items)
        self.all_items.sort()
        self.all_formatted_items = [item.replace("_", " ").title() for item in self.all_items]

        self.all_effects = []
        for category_effects in EFFECT_CATEGORIES.values():
            self.all_effects.extend(category_effects)
        self.all_effects.sort()
        self.all_formatted_effects = [effect.replace("_", " ").title() for effect in self.all_effects]

        # Ensure the directory for the favorites file exists
        os.makedirs(os.path.dirname(self.FAVORITES_FILE), exist_ok=True)

        # Load favorites from file
        self.favorite_commands = self.load_favorites()

    def bind_horizontal_scroll(self, event):
        """
        Bind the mouse wheel event to enable horizontal scrolling.
        """
        self.command_slider_frame._parent_canvas.bind_all("<MouseWheel>", self.scroll_horizontally)

    def unbind_horizontal_scroll(self, event):
        """
        Unbind the mouse wheel event when the cursor leaves the frame.
        """
        self.command_slider_frame._parent_canvas.unbind_all("<MouseWheel>")

    def scroll_horizontally(self, event):
        """
        Scroll the command slider horizontally based on mouse wheel movement.
        """
        scroll_speed = 20  # Increased scroll speed multiplier
        self.command_slider_frame._parent_canvas.xview_scroll(-int(event.delta / 120 * scroll_speed), "units")

    def add_command_buttons(self):
        """
        Add command buttons to the slider, sorted alphabetically, with favorite functionality.
        """
        # Clear existing buttons
        for widget in self.command_slider_frame.winfo_children():
            widget.destroy()

        # Sort commands alphabetically, with favorites first
        sorted_commands = sorted(COMMAND_TYPES.keys(), key=lambda c: (c not in self.favorite_commands, c.lower()))

        for command_type in sorted_commands:
            frame = ctk.CTkFrame(self.command_slider_frame, height=30, width=130)
            frame.pack(side="left", padx=5, pady=5)

            # Create the main command button
            button = ctk.CTkButton(
                frame,
                text=command_type.capitalize(),
                width=100,
                height=30,
                command=partial(self.on_command_change, command_type),
            )
            button.pack(side="left")

            # Create the favorite button with the correct star icon
            favorite_button = ctk.CTkButton(
                frame,
                text="⭐" if command_type in self.favorite_commands else "☆",
                width=30,
                height=30,
                command=partial(self.toggle_favorite, command_type),
            )
            favorite_button.pack(side="left")

    def toggle_favorite(self, command_type: str):
        """
        Toggle the favorite status of a command.
        """
        if command_type in self.favorite_commands:
            self.favorite_commands.remove(command_type)
        else:
            self.favorite_commands.add(command_type)

        # Save favorites to file
        self.save_favorites()

        # Refresh the command buttons to reflect the updated favorites
        self.add_command_buttons()

    def open_settings(self):
        """
        Open the settings page (placeholder for now).
        """
        print("Settings button clicked!")

    def show_home_page(self):
        """
        Display the home page with all command options as buttons.
        """
        # Clear previous UI
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()

        # Clear the command output and feedback
        self.command_text.delete("1.0", "end")
        self.feedback_text.delete("1.0", "end")
        self.add_command_buttons()

    def on_command_type_change(self, *args):
        """
        Handle changes to the command type input box and update the UI.
        """
        selected_command = self.command_type_var.get()
        if selected_command:
            self.on_command_change(selected_command)
        else:
            self.show_home_page()

    def on_command_change(self, command_type: str) -> None:
        """
        Handle changes to the selected command type.

        Args:
            command_type (str): The selected command type.
        """
        self.command_type_var.set(command_type)  # Update the dropdown value

        # Clear previous command UI
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()

        # Create new command UI based on the selected type
        if command_type:
            command_data = COMMAND_TYPES[command_type]
            if command_type == "give":
                self.current_command = GiveCommand(self.parameters_frame, command_data, self.all_formatted_items, self.version_var)
            elif command_type == "effect":
                self.current_command = EffectCommand(self.parameters_frame, command_data)
            elif command_type == "gamemode":
                self.current_command = GamemodeCommand(self.parameters_frame, command_data)
            elif command_type == "tp":
                self.current_command = TeleportCommand(self.parameters_frame, command_data)

            # Set up command update callback
            if self.current_command:
                self.current_command.on_parameter_change = self.update_command
        else:
            self.current_command = None

        # Update the command output
        self.update_command()

    def on_version_change(self, *args):
        """
        Handle changes to the selected Minecraft version.

        Args:
            version (str): The selected Minecraft version.
        """

        if hasattr(self, "current_command") and isinstance(self.current_command, GiveCommand):
            self.current_command.on_version_change(self.version_var.get())
        # Update the command if needed
        if self.current_command:
            self.update_command()

    def update_command(self, event=None) -> None:
        """
        Update the command output and feedback based on the current parameters.
        """
        if not self.current_command:
            self.command_text.delete("1.0", "end")
            self.feedback_text.delete("1.0", "end")
            return

        # Update the command text
        command = self.current_command.update_command()
        self.command_text.delete("1.0", "end")
        self.command_text.insert("1.0", command)

        # Update the feedback text
        feedback = self.current_command.get_feedback()
        self.feedback_text.delete("1.0", "end")
        self.feedback_text.insert("1.0", "\n".join(feedback))

    def load_favorites(self) -> set:
        """
        Load favorite commands from a JSON file.
        If the file doesn't exist, create it with an empty set.
        Returns:
            set: A set of favorite commands.
        """
        if not os.path.exists(self.FAVORITES_FILE):
            # Create an empty JSON file if it doesn't exist
            with open(self.FAVORITES_FILE, "w") as file:
                json.dump([], file)
            return set()

        try:
            with open(self.FAVORITES_FILE, "r") as file:
                return set(json.load(file))
        except (json.JSONDecodeError, IOError):
            print("Failed to load favorites. Starting with an empty set.")
            return set()

    def save_favorites(self):
        """
        Save favorite commands to a JSON file.
        """
        try:
            with open(self.FAVORITES_FILE, "w") as file:
                json.dump(list(self.favorite_commands), file)
        except IOError:
            print("Failed to save favorites.")

if __name__ == "__main__":
    app = MinecraftCommandGenerator()
    app.mainloop()

