from typing import Dict, Any

class CommandSummarizer:
    """A class that generates human-readable summaries of Minecraft commands."""
    
    @staticmethod
    def summarize(command_type: str, params: Dict[str, Any]) -> str:
        """Generate a concise summary of what a command does."""
        summaries = {
            "give": lambda p: f"🎁 Gives {p.get('amount', '1')}x {p.get('item', 'item')} to {p.get('player', 'target')}",
            "tp": lambda p: f"🚀 Teleports {p.get('player', 'target')} to {p.get('x', 'X')} {p.get('y', 'Y')} {p.get('z', 'Z')}",
            "gamemode": lambda p: f"🎮 Changes {p.get('player', 'target')}'s game mode to {p.get('mode', 'selected mode')}",
            "effect": lambda p: f"✨ Applies {p.get('effect', 'effect')} (Level {p.get('amplifier', '0')}) to {p.get('player', 'target')} for {p.get('duration', '0')} seconds",
            "time": lambda p: f"⏰ Sets game time to {p.get('value', 'specified time')}",
            "weather": lambda p: f"🌤️ Changes weather to {p.get('type', 'specified type')} for {p.get('duration', 'default')} seconds",
            "difficulty": lambda p: f"⚔️ Sets game difficulty to {p.get('level', 'specified level')}",
            "gamerule": lambda p: f"⚙️ Changes {p.get('rule', 'game rule')} to {p.get('value', 'specified value')}",
            "enchant": lambda p: f"🔮 Enchants {p.get('player', 'target')}'s item with {p.get('enchantment', 'enchantment')} {p.get('level', '1')}",
            "kill": lambda p: f"💀 Kills {p.get('target', 'target entity')}",
            "clear": lambda p: f"🗑️ Clears {p.get('amount', 'all')} {p.get('item', 'items')} from {p.get('player', 'target')}'s inventory",
            "fill": lambda p: f"🏗️ Fills area from ({p.get('x1', 'X1')}, {p.get('y1', 'Y1')}, {p.get('z1', 'Z1')}) to ({p.get('x2', 'X2')}, {p.get('y2', 'Y2')}, {p.get('z2', 'Z2')}) with {p.get('block', 'specified block')}"
        }
        
        if command_type in summaries:
            return summaries[command_type](params)
        return f"Executes the {command_type} command with specified parameters" 