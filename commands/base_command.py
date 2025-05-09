import customtkinter as ctk
from typing import Dict, Any, List, Optional
from minecraft_data import COMMAND_TYPES, TARGET_SELECTORS
from command_summarizer import CommandSummarizer

class BaseCommand:
    """Base class for all Minecraft commands."""
    
    def __init__(self, master: ctk.CTkFrame, command_type: str, command_data: Dict[str, Any]):
        """
        Initialize the command with its type and parameters.
        
        Args:
            master (CTkFrame): Parent frame for the command UI.
            command_type (str): Type of the command (e.g., "give", "tp").
            command_data (Dict[str, Any]): Metadata and configuration for the command.
        """
        self.master = master
        self.command_type = command_type
        self.command_data = command_data
        self.parameter_vars: Dict[str, Any] = {}
        
        # Create a frame for the command parameters
        self.param_frame = ctk.CTkFrame(self.master)
        self.param_frame.pack(fill="x", padx=5, pady=5)
        
        # Let child classes set up their UI
        self.setup_ui()
        
        # Initialize feedback
        self.on_parameter_change(None)
    
    def setup_ui(self) -> None:
        """Set up the UI elements for the command. To be overridden by child classes."""
        pass
    
    def create_parameter_ui(self, param_name: str) -> None:
        """
        Create UI elements for a specific parameter.
        
        Args:
            param_name (str): Name of the parameter to create UI for.
        """
        # Create a frame for this parameter
        param_frame = ctk.CTkFrame(self.param_frame)
        param_frame.pack(fill="x", padx=5, pady=2)
        
        # Add parameter label
        label = ctk.CTkLabel(param_frame, text=f"{param_name.capitalize()}:")
        label.pack(side="left", padx=5)
        
        # Create entry field
        entry = ctk.CTkEntry(param_frame)
        entry.pack(side="left", fill="x", expand=True, padx=5)
        entry.bind("<KeyRelease>", self.on_parameter_change)
        
        # Store the entry widget
        self.parameter_vars[param_name] = entry
        
        # Add preset dropdown if available
        if "presets" in self.command_data and param_name in self.command_data["presets"]:
            self.create_preset_dropdown(param_frame, param_name)
    
    def create_preset_dropdown(self, frame: ctk.CTkFrame, param_name: str) -> None:
        """
        Create a dropdown menu for parameter presets.
        
        Args:
            frame (CTkFrame): Parent frame for the dropdown.
            param_name (str): Name of the parameter associated with the dropdown.
        """
        dropdown = ctk.CTkOptionMenu(
            frame,
            values=self.command_data["presets"][param_name],
            command=lambda value: self.on_preset_selected(param_name, value)
        )
        dropdown.pack(side="left", padx=5)
    
    def create_target_selector(self, frame: ctk.CTkFrame, param_name: str) -> None:
        """
        Create a target selector UI element.
        
        Args:
            frame (CTkFrame): Parent frame for the target selector.
            param_name (str): Name of the parameter associated with the selector.
        """
        # Create a new frame for the target selector
        selector_frame = ctk.CTkFrame(frame)
        selector_frame.pack(fill="x", padx=5, pady=2)
        
        # Add label
        label = ctk.CTkLabel(selector_frame, text=f"{param_name.capitalize()}:")
        label.pack(side="left", padx=5)
        
        # Create entry field
        entry = ctk.CTkEntry(selector_frame)
        entry.pack(side="left", fill="x", expand=True, padx=5)
        entry.bind("<KeyRelease>", self.on_parameter_change)
        
        # Create dropdown for target selectors
        selector_var = ctk.StringVar()
        dropdown = ctk.CTkOptionMenu(
            selector_frame,
            values=TARGET_SELECTORS,
            variable=selector_var,
            command=lambda value: self.on_selector_selected(param_name, value)
        )
        dropdown.pack(side="left", padx=5)
        
        # Store the widgets
        self.parameter_vars[param_name] = {
            "selector": selector_var,
            "entry": entry
        }
    
    def on_parameter_change(self, event: Optional[Any] = None) -> None:
        """Handle changes to parameter values."""
        self.update_command()
    
    def on_preset_selected(self, param_name: str, value: str) -> None:
        """
        Handle selection of a preset value.
        
        Args:
            param_name (str): Name of the parameter.
            value (str): Selected preset value.
        """
        if param_name in self.parameter_vars:
            self.parameter_vars[param_name].delete(0, "end")
            self.parameter_vars[param_name].insert(0, value)
            self.update_command()
    
    def on_selector_selected(self, param_name: str, value: str) -> None:
        """
        Handle selection of a target selector.
        
        Args:
            param_name (str): Name of the parameter.
            value (str): Selected target selector.
        """
        if param_name in self.parameter_vars:
            self.parameter_vars[param_name]["entry"].delete(0, "end")
            self.parameter_vars[param_name]["entry"].insert(0, value)
            self.update_command()
    
    def get_parameter_value(self, param_name: str) -> str:
        """
        Get the current value of a parameter.
        
        Args:
            param_name (str): Name of the parameter.
        
        Returns:
            str: Current value of the parameter.
        """
        if param_name in self.parameter_vars:
            if isinstance(self.parameter_vars[param_name], dict):
                return self.parameter_vars[param_name]["entry"].get()
            return self.parameter_vars[param_name].get()
        return ""
    
    def get_feedback(self) -> List[str]:
        """
        Get feedback about the current command state.
        
        Returns:
            List[str]: Feedback messages.
        """
        feedback = []
        
        # Get current parameter values
        params = {param: self.get_parameter_value(param) for param in self.command_data["parameters"]}
        
        # Add command summary using CommandSummarizer
        feedback.append(CommandSummarizer.summarize(self.command_type, params))
        feedback.append("")
        
        # Add parameter feedback
        for param in self.command_data["parameters"]:
            value = params[param]
            if value:
                feedback.append(f"{param.capitalize()}: {value}")
            elif param in self.command_data["feedback"]:
                feedback.append(f"{param.capitalize()}: {self.command_data['feedback'][param]}")
        
        return feedback
    
    def update_command(self) -> None:
        """Update the command output based on current parameter values."""
        pass  # To be implemented by subclasses

