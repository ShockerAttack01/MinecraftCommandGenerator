from typing import Dict, Any

class CommandSummarizer:
    """A class that generates human-readable summaries of Minecraft commands."""
    
    @staticmethod
    def summarize(command_type: str, params: Dict[str, Any]) -> str:
        """
        Generate a concise summary of what a command does.
        
        Args:
            command_type (str): The type of the command (e.g., "give", "tp").
            params (Dict[str, Any]): Parameters for the command.
        
        Returns:
            str: A human-readable summary of the command.
        """
        if command_type == "give":
            item = params.get("item", "item")
            amount = params.get("amount", 1)
            player = params.get("player", "target")
            return f"🎁 Gives {amount}x {item} to {player}."

        elif command_type == "tp":
            player = params.get("player", "target")
            x = params.get("x", "~")
            y = params.get("y", "~")
            z = params.get("z", "~")
            return f"🚀 Teleports {player} to coordinates ({x}, {y}, {z})."

        elif command_type == "gamemode":
            player = params.get("player", "target")
            mode = params.get("mode", "selected mode")
            return f"🎮 Changes {player}'s game mode to {mode}."

        elif command_type == "effect":
            player = params.get("player", "target")
            effect = params.get("effect", "effect")
            duration = params.get("duration", "0")
            amplifier = params.get("amplifier", "0")
            return f"✨ Applies {effect} (Level {amplifier}) to {player} for {duration} seconds."

        elif command_type == "time":
            action = params.get("action", "set")
            value = params.get("value", "specified time")
            return f"⏰ {action.capitalize()}s the game time to {value}."
        
        elif command_type == "weather":
            weather_type = params.get("type", "clear")
            duration = params.get("duration", "default")
            return f"🌤️ Changes the weather to {weather_type} for {duration} seconds."

        elif command_type == "difficulty":
            level = params.get("level", "normal")
            return f"⚔️ Sets the game difficulty to {level}."

        elif command_type == "gamerule":
            rule = params.get("rule", "game rule")
            value = params.get("value", "true")
            return f"⚙️ Changes the game rule '{rule}' to {value}."

        elif command_type == "enchant":
            player = params.get("player", "target")
            enchantment = params.get("enchantment", "enchantment")
            level = params.get("level", 1)
            return f"🔮 Enchants {player}'s item with {enchantment} at level {level}."

        elif command_type == "kill":
            target = params.get("target", "target entity")
            return f"💀 Kills {target}."

        elif command_type == "clear":
            player = params.get("player", "target")
            item = params.get("item", "items")
            amount = params.get("amount", "all")
            return f"🗑️ Clears {amount} {item} from {player}'s inventory."

        elif command_type == "fill":
            x1, y1, z1 = params.get("x1", "~"), params.get("y1", "~"), params.get("z1", "~")
            x2, y2, z2 = params.get("x2", "~"), params.get("y2", "~"), params.get("z2", "~")
            block = params.get("block", "specified block")
            return f"🏗️ Fills the area from ({x1}, {y1}, {z1}) to ({x2}, {y2}, {z2}) with {block}."

        # Default summary for unknown commands
        return f"Executes the {command_type} command with specified parameters."
