import customtkinter as ctk
from typing import Dict, List, Tuple, Any
from .base_command import BaseCommand
from minecraft_data import TARGET_SELECTORS, EFFECT_CATEGORIES
import re

class EffectCommand(BaseCommand):
    def __init__(self, master: ctk.CTkFrame, command_data: Dict[str, Any], all_formatted_effects: List[str]):
        self.all_formatted_effects = all_formatted_effects
        super().__init__(master, command_data)
        
    def setup_ui(self):
        # Player parameter
        player_frame = self.create_parameter_frame("player")
        self.create_target_selector(player_frame, "player")
        
        # Effect parameter
        effect_frame = self.create_parameter_frame("effect")
        effect_input_frame = ctk.CTkFrame(effect_frame)
        effect_input_frame.pack(side="left", fill="x", expand=True, padx=5)
        
        # Add search box
        from minecraft_command_generator import SearchBox  # Import here to avoid circular imports
        search_box = SearchBox(
            effect_input_frame,
            self.all_formatted_effects,
            command=lambda v: self.on_parameter_change()
        )
        search_box.pack(side="left", fill="x", expand=True)
        
        # Add category dropdown
        category_var = ctk.StringVar(value="Select Category")
        category_dropdown = ctk.CTkOptionMenu(
            effect_input_frame,
            values=["Select Category"] + list(EFFECT_CATEGORIES.keys()),
            variable=category_var,
            command=lambda v, s=search_box: self.on_category_change(v, s)
        )
        category_dropdown.pack(side="left", padx=(5, 0))
        
        self.parameter_vars["effect"] = (category_var, search_box)
        
        # Duration parameter
        duration_frame = self.create_parameter_frame("duration")
        duration_var, duration_entry = self.create_entry_with_dropdown(
            duration_frame,
            "duration",
            ["1", "5", "10", "30", "60", "120", "300", "600"]
        )
        self.parameter_vars["duration"] = (duration_var, duration_entry)
        
        # Amplifier parameter
        amplifier_frame = self.create_parameter_frame("amplifier")
        amplifier_var, amplifier_entry = self.create_entry_with_dropdown(
            amplifier_frame,
            "amplifier",
            ["0", "1", "2", "3", "4", "5"]
        )
        self.parameter_vars["amplifier"] = (amplifier_var, amplifier_entry)
        
        # Hide particles parameter
        hide_particles_frame = self.create_parameter_frame("hide_particles")
        hide_particles_var = ctk.StringVar(value="false")
        hide_particles_dropdown = ctk.CTkOptionMenu(
            hide_particles_frame,
            values=["false", "true"],
            variable=hide_particles_var,
            command=lambda v: self.on_parameter_change()
        )
        hide_particles_dropdown.pack(side="left", fill="x", expand=True, padx=5)
        self.parameter_vars["hide_particles"] = hide_particles_var
        
    def on_category_change(self, category: str, search_box: Any):
        if category == "Select Category":
            search_box.set_items(self.all_formatted_effects)
        else:
            effects = EFFECT_CATEGORIES[category]
            formatted_effects = [effect.replace("_", " ").title() for effect in effects]
            search_box.set_items(formatted_effects)
            
    def get_command(self) -> str:
        command_parts = ["effect"]
        
        # Player
        selector_var, entry = self.parameter_vars["player"]
        player = entry.get()
        if player:
            command_parts.append(player)
            
        # Effect
        category_var, search_box = self.parameter_vars["effect"]
        effect = search_box.get().lower().replace(" ", "_")
        if effect:
            command_parts.append(effect)
            
        # Duration
        duration_var, duration_entry = self.parameter_vars["duration"]
        duration = duration_entry.get()
        if duration:
            command_parts.append(duration)
            
        # Amplifier
        amplifier_var, amplifier_entry = self.parameter_vars["amplifier"]
        amplifier = amplifier_entry.get()
        if amplifier:
            command_parts.append(amplifier)
            
        # Hide particles
        hide_particles = self.parameter_vars["hide_particles"].get()
        if hide_particles == "true":
            command_parts.append("true")
            
        return " ".join(command_parts)
        
    def get_feedback(self) -> List[str]:
        feedback = []
        command_parts = self.get_command().split()
        
        # Basic validation
        if len(command_parts) < 3:
            feedback.append("⚠️ Command is incomplete. Please fill in player and effect.")
            return feedback
            
        # Add command description
        feedback.append(f"📝 {self.command_data['description']}")
        feedback.append("")
        
        # Player validation
        player = command_parts[1]
        if not (player in TARGET_SELECTORS or re.match(r"^[a-zA-Z0-9_]{1,16}$", player)):
            feedback.append("⚠️ Invalid player/target selector. Must be a valid player name or target selector (@a, @p, @e, @r, @s).")
            
        # Effect validation
        effect_id = command_parts[2]
        if not re.match(r"^[a-z0-9_]+$", effect_id):
            feedback.append("⚠️ Invalid effect ID. Must be lowercase letters, numbers, and underscores only.")
            
        # Duration validation
        if len(command_parts) > 3 and not command_parts[3].isdigit():
            feedback.append("⚠️ Duration must be a number.")
            
        # Amplifier validation
        if len(command_parts) > 4 and not command_parts[4].isdigit():
            feedback.append("⚠️ Amplifier must be a number.")
            
        # Find effect in categories and show formatted name
        effect_found = False
        for category, effects in EFFECT_CATEGORIES.items():
            if effect_id in effects:
                effect_found = True
                formatted_name = effect_id.replace("_", " ").title()
                duration = command_parts[3] if len(command_parts) > 3 else "1"
                amplifier = command_parts[4] if len(command_parts) > 4 else "0"
                feedback.append(f"✨ Effect: {formatted_name}")
                feedback.append(f"⏱️ Duration: {duration} seconds")
                feedback.append(f"📊 Amplifier: {amplifier}")
                feedback.append(f"📦 Category: {category}")
                break
                
        if not effect_found and effect_id:
            feedback.append("⚠️ Unknown effect ID. Please select an effect from the search box.")
            
        if not feedback or (len(feedback) == 1 and feedback[0].startswith("📝")):
            feedback.append("✅ Command looks valid!")
            feedback.append("")
            feedback.append("Parameters:")
            for param in self.command_data["parameters"]:
                if param in self.command_data["feedback"]:
                    feedback.append(f"• {param}: {self.command_data['feedback'][param]}")
                    
        return feedback 