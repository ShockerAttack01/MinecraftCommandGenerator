import customtkinter as ctk
from typing import List, Optional

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
