import customtkinter as ctk
from typing import Dict, List, Tuple, Any
from .base_command import BaseCommand
from minecraft_data import TARGET_SELECTORS
import re

class TeleportCommand(BaseCommand):
    def __init__(self, master: ctk.CTkFrame, command_data: Dict[str, Any]):
        super().__init__(master, command_data)
        
    def setup_ui(self):
        # Target parameter
        target_frame = self.create_parameter_frame("target")
        self.create_target_selector(target_frame, "target")
        
        # Destination parameter
        dest_frame = self.create_parameter_frame("destination")
        self.create_target_selector(dest_frame, "destination")
        
        # Coordinates parameters
        coords_frame = self.create_parameter_frame("coordinates")
        coords_input_frame = ctk.CTkFrame(coords_frame)
        coords_input_frame.pack(side="left", fill="x", expand=True, padx=5)
        
        # X coordinate
        x_frame = ctk.CTkFrame(coords_input_frame)
        x_frame.pack(side="left", fill="x", expand=True, padx=(0, 5))
        x_label = ctk.CTkLabel(x_frame, text="X:")
        x_label.pack(side="left", padx=(5, 0))
        x_entry = ctk.CTkEntry(x_frame, width=60)
        x_entry.pack(side="left", fill="x", expand=True, padx=5)
        x_entry.bind("<KeyRelease>", lambda e: self.on_parameter_change())
        
        # Y coordinate
        y_frame = ctk.CTkFrame(coords_input_frame)
        y_frame.pack(side="left", fill="x", expand=True, padx=(0, 5))
        y_label = ctk.CTkLabel(y_frame, text="Y:")
        y_label.pack(side="left", padx=(5, 0))
        y_entry = ctk.CTkEntry(y_frame, width=60)
        y_entry.pack(side="left", fill="x", expand=True, padx=5)
        y_entry.bind("<KeyRelease>", lambda e: self.on_parameter_change())
        
        # Z coordinate
        z_frame = ctk.CTkFrame(coords_input_frame)
        z_frame.pack(side="left", fill="x", expand=True)
        z_label = ctk.CTkLabel(z_frame, text="Z:")
        z_label.pack(side="left", padx=(5, 0))
        z_entry = ctk.CTkEntry(z_frame, width=60)
        z_entry.pack(side="left", fill="x", expand=True, padx=5)
        z_entry.bind("<KeyRelease>", lambda e: self.on_parameter_change())
        
        self.parameter_vars["coordinates"] = (x_entry, y_entry, z_entry)
        
        # Rotation parameters
        rotation_frame = self.create_parameter_frame("rotation")
        rotation_input_frame = ctk.CTkFrame(rotation_frame)
        rotation_input_frame.pack(side="left", fill="x", expand=True, padx=5)
        
        # Yaw (horizontal rotation)
        yaw_frame = ctk.CTkFrame(rotation_input_frame)
        yaw_frame.pack(side="left", fill="x", expand=True, padx=(0, 5))
        yaw_label = ctk.CTkLabel(yaw_frame, text="Yaw:")
        yaw_label.pack(side="left", padx=(5, 0))
        yaw_entry = ctk.CTkEntry(yaw_frame, width=60)
        yaw_entry.pack(side="left", fill="x", expand=True, padx=5)
        yaw_entry.bind("<KeyRelease>", lambda e: self.on_parameter_change())
        
        # Pitch (vertical rotation)
        pitch_frame = ctk.CTkFrame(rotation_input_frame)
        pitch_frame.pack(side="left", fill="x", expand=True)
        pitch_label = ctk.CTkLabel(pitch_frame, text="Pitch:")
        pitch_label.pack(side="left", padx=(5, 0))
        pitch_entry = ctk.CTkEntry(pitch_frame, width=60)
        pitch_entry.pack(side="left", fill="x", expand=True, padx=5)
        pitch_entry.bind("<KeyRelease>", lambda e: self.on_parameter_change())
        
        self.parameter_vars["rotation"] = (yaw_entry, pitch_entry)
        
    def get_command(self) -> str:
        command_parts = ["tp"]
        
        # Target
        selector_var, entry = self.parameter_vars["target"]
        target = entry.get()
        if target:
            command_parts.append(target)
            
        # Destination
        dest_selector_var, dest_entry = self.parameter_vars["destination"]
        destination = dest_entry.get()
        if destination:
            command_parts.append(destination)
            
        # Coordinates
        x_entry, y_entry, z_entry = self.parameter_vars["coordinates"]
        x = x_entry.get()
        y = y_entry.get()
        z = z_entry.get()
        if x and y and z:
            command_parts.extend([x, y, z])
            
            # Rotation
            yaw_entry, pitch_entry = self.parameter_vars["rotation"]
            yaw = yaw_entry.get()
            pitch = pitch_entry.get()
            if yaw and pitch:
                command_parts.extend([yaw, pitch])
                
        return " ".join(command_parts)
        
    def get_feedback(self) -> List[str]:
        feedback = []
        command_parts = self.get_command().split()
        
        # Basic validation
        if len(command_parts) < 2:
            feedback.append("⚠️ Command is incomplete. Please specify a target.")
            return feedback
            
        # Add command description
        feedback.append(f"📝 {self.command_data['description']}")
        feedback.append("")
        
        # Target validation
        target = command_parts[1]
        if not (target in TARGET_SELECTORS or re.match(r"^[a-zA-Z0-9_]{1,16}$", target)):
            feedback.append("⚠️ Invalid target. Must be a valid player name or target selector (@a, @p, @e, @r, @s).")
        else:
            feedback.append(f"👤 Target: {target}")
            
        # Destination validation
        if len(command_parts) > 2:
            destination = command_parts[2]
            if destination in TARGET_SELECTORS or re.match(r"^[a-zA-Z0-9_]{1,16}$", destination):
                feedback.append(f"🎯 Destination: {destination}")
            elif len(command_parts) >= 5:  # Coordinates provided
                try:
                    x = float(command_parts[2])
                    y = float(command_parts[3])
                    z = float(command_parts[4])
                    feedback.append(f"📍 Coordinates: X={x}, Y={y}, Z={z}")
                    
                    # Rotation validation
                    if len(command_parts) >= 7:
                        try:
                            yaw = float(command_parts[5])
                            pitch = float(command_parts[6])
                            feedback.append(f"🔄 Rotation: Yaw={yaw}°, Pitch={pitch}°")
                        except ValueError:
                            feedback.append("⚠️ Invalid rotation values. Yaw and pitch must be numbers.")
                except ValueError:
                    feedback.append("⚠️ Invalid coordinate values. X, Y, and Z must be numbers.")
            else:
                feedback.append("⚠️ Invalid destination. Must be a player name, target selector, or coordinates.")
                
        if not feedback or (len(feedback) == 1 and feedback[0].startswith("📝")):
            feedback.append("✅ Command looks valid!")
            feedback.append("")
            feedback.append("Parameters:")
            for param in self.command_data["parameters"]:
                if param in self.command_data["feedback"]:
                    feedback.append(f"• {param}: {self.command_data['feedback'][param]}")
                    
        return feedback 