import customtkinter as ctk
from typing import Dict, List, Tuple, Any, Optional
import re
from minecraft_data import (
    TARGET_SELECTORS,
    VERSIONS,
    EFFECT_CATEGORIES,
    ITEM_CATEGORIES,
    COMMAND_TYPES
)
from commands import (
    GiveCommand,
    EffectCommand,
    GamemodeCommand,
    TeleportCommand
)

class SearchBox(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkFrame, items: List[str], command: Optional[callable] = None):
        super().__init__(master)
        self.items = items
        self.command = command
        
        # Create entry field
        self.entry = ctk.CTkEntry(self)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<KeyRelease>", self.on_key_release)
        self.entry.bind("<FocusIn>", self.on_focus_in)
        self.entry.bind("<FocusOut>", self.on_focus_out)
        
        # Create suggestions frame
        self.suggestions_frame = ctk.CTkFrame(self)
        self.suggestions_frame.pack(side="left", fill="x", expand=True)
        
        # Create scrollable frame for suggestions
        self.scrollable_frame = ctk.CTkScrollableFrame(self.suggestions_frame)
        self.scrollable_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Create suggestion buttons
        self.suggestion_buttons = []
        self.update_suggestions(self.items)
        
    def on_key_release(self, event):
        text = self.entry.get().lower()
        if not text:
            self.update_suggestions(self.items)
        else:
            filtered_items = [item for item in self.items if text in item.lower()]
            self.update_suggestions(filtered_items)
            
        if self.command:
            self.command(self.entry.get())
            
    def on_focus_in(self, event):
        self.update_suggestions(self.items)
        
    def on_focus_out(self, event):
        self.suggestions_frame.pack_forget()
        
    def update_suggestions(self, items: List[str]):
        # Clear existing buttons
        for button in self.suggestion_buttons:
            button.destroy()
        self.suggestion_buttons.clear()
        
        # Create new buttons
        for item in items:
            button = ctk.CTkButton(
                self.scrollable_frame,
                text=item,
                command=lambda i=item: self.select_item(i),
                height=30
            )
            button.pack(fill="x", pady=2)
            self.suggestion_buttons.append(button)
            
        # Show/hide suggestions frame
        if items:
            self.suggestions_frame.pack(side="left", fill="x", expand=True)
        else:
            self.suggestions_frame.pack_forget()
            
    def select_item(self, item: str):
        self.entry.delete(0, "end")
        self.entry.insert(0, item)
        self.update_suggestions(self.items)
        if self.command:
            self.command(item)
            
    def get(self) -> str:
        return self.entry.get()
        
    def set_items(self, items: List[str]):
        self.items = items
        self.update_suggestions(items)

class MinecraftCommandGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Minecraft Command Generator")
        self.geometry("1200x800")  # Increased window size
        
        # Create main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Create command type selector
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
        
        # Create version selector
        self.version_frame = ctk.CTkFrame(self.main_frame)
        self.version_frame.pack(fill="x", padx=5, pady=5)
        
        self.version_label = ctk.CTkLabel(self.version_frame, text="Minecraft Version:")
        self.version_label.pack(side="left", padx=5)
        
        self.version_var = ctk.StringVar(value=VERSIONS[0])
        self.version_dropdown = ctk.CTkOptionMenu(
            self.version_frame,
            values=VERSIONS,
            variable=self.version_var,
            command=self.on_version_change
        )
        self.version_dropdown.pack(side="left", padx=5)
        
        # Create parameters frame
        self.parameters_frame = ctk.CTkFrame(self.main_frame)
        self.parameters_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Create command output frame
        self.command_frame = ctk.CTkFrame(self.main_frame)
        self.command_frame.pack(fill="x", padx=5, pady=5)
        
        self.command_label = ctk.CTkLabel(self.command_frame, text="Command:")
        self.command_label.pack(side="left", padx=5)
        
        self.command_text = ctk.CTkTextbox(self.command_frame, height=50)
        self.command_text.pack(side="left", fill="x", expand=True, padx=5)
        
        # Create feedback frame
        self.feedback_frame = ctk.CTkFrame(self.main_frame)
        self.feedback_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.feedback_label = ctk.CTkLabel(self.feedback_frame, text="Feedback:")
        self.feedback_label.pack(side="left", padx=5)
        
        self.feedback_text = ctk.CTkTextbox(self.feedback_frame, height=200)  # Increased height
        self.feedback_text.pack(side="left", fill="both", expand=True, padx=5)
        
        # Initialize command instance
        self.current_command = None
        
        # Preload all items and effects
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
        
    def on_command_change(self, command_type: str):
        """Handle command type change."""
        # Clear previous command UI
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        
        # Create new command UI
        if command_type:
            command_data = COMMAND_TYPES[command_type]
            if command_type == "give":
                self.current_command = GiveCommand(self.parameters_frame, command_data, self.all_formatted_items)
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
        
        # Update command output
        self.update_command()
        
    def on_version_change(self, version: str):
        """Handle version change."""
        # Update command if needed
        if self.current_command:
            self.update_command()
            
    def update_command(self, event=None):
        """Update the command output and feedback."""
        if not self.current_command:
            self.command_text.delete("1.0", "end")
            self.feedback_text.delete("1.0", "end")
            return
            
        # Update command text
        command = self.current_command.update_command()
        self.command_text.delete("1.0", "end")
        self.command_text.insert("1.0", command)
        
        # Update feedback
        feedback = self.current_command.get_feedback()
        self.feedback_text.delete("1.0", "end")
        self.feedback_text.insert("1.0", "\n".join(feedback))

if __name__ == "__main__":
    app = MinecraftCommandGenerator()
    app.mainloop() 