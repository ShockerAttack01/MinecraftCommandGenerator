import customtkinter as ctk
from typing import Dict, List, Tuple, Any
from .base_command import BaseCommand
from minecraft_data import TARGET_SELECTORS
import re

class GamemodeCommand(BaseCommand):
    def __init__(self, master: ctk.CTkFrame, command_data: Dict[str, Any]):
        super().__init__(master, command_data)
        
    def setup_ui(self):
        # Player parameter
        player_frame = self.create_parameter_frame("player")
        self.create_target_selector(player_frame, "player")
        
        # Gamemode parameter
        gamemode_frame = self.create_parameter_frame("gamemode")
        gamemode_var = ctk.StringVar(value="")
        gamemode_dropdown = ctk.CTkOptionMenu(
            gamemode_frame,
            values=["", "survival", "creative", "adventure", "spectator"],
            variable=gamemode_var,
            command=lambda v: self.on_parameter_change()
        )
        gamemode_dropdown.pack(side="left", fill="x", expand=True, padx=5)
        self.parameter_vars["gamemode"] = gamemode_var
        
    def get_command(self) -> str:
        command_parts = ["gamemode"]
        
        # Gamemode
        gamemode = self.parameter_vars["gamemode"].get()
        if gamemode:
            command_parts.append(gamemode)
            
        # Player
        selector_var, entry = self.parameter_vars["player"]
        player = entry.get()
        if player:
            command_parts.append(player)
            
        return " ".join(command_parts)
        
    def get_feedback(self) -> List[str]:
        feedback = []
        command_parts = self.get_command().split()
        
        # Basic validation
        if len(command_parts) < 2:
            feedback.append("⚠️ Command is incomplete. Please select a gamemode.")
            return feedback
            
        # Add command description
        feedback.append(f"📝 {self.command_data['description']}")
        feedback.append("")
        
        # Gamemode validation
        gamemode = command_parts[1]
        valid_gamemodes = ["survival", "creative", "adventure", "spectator"]
        if gamemode not in valid_gamemodes:
            feedback.append("⚠️ Invalid gamemode. Must be one of: survival, creative, adventure, spectator")
        else:
            feedback.append(f"🎮 Gamemode: {gamemode.title()}")
            
        # Player validation
        if len(command_parts) > 2:
            player = command_parts[2]
            if not (player in TARGET_SELECTORS or re.match(r"^[a-zA-Z0-9_]{1,16}$", player)):
                feedback.append("⚠️ Invalid player/target selector. Must be a valid player name or target selector (@a, @p, @e, @r, @s).")
            else:
                feedback.append(f"👤 Target: {player}")
        else:
            feedback.append("⚠️ No player specified. The command will affect the executing player.")
            
        if not feedback or (len(feedback) == 1 and feedback[0].startswith("📝")):
            feedback.append("✅ Command looks valid!")
            feedback.append("")
            feedback.append("Parameters:")
            for param in self.command_data["parameters"]:
                if param in self.command_data["feedback"]:
                    feedback.append(f"• {param}: {self.command_data['feedback'][param]}")
                    
        return feedback 