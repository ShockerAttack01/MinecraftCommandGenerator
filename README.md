# Minecraft Command Generator

A user-friendly GUI application for generating Minecraft commands with version-specific support and real-time feedback.

## Features

- Support for multiple Minecraft versions (1.16 - 1.20.4)
- Real-time command preview
- Command validation and feedback
- Command history tracking
- Modern, dark-themed interface
- Support for common commands:
  - give
  - tp (teleport)
  - gamemode
  - effect

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python minecraft_command_generator.py
```

2. Select your Minecraft version from the dropdown menu
3. Choose the command type you want to generate
4. Fill in the required parameters
5. The command preview and feedback will update in real-time
6. Copy the generated command from the preview section

## Command Types

### Give Command
- Parameters:
  - player: Target player name
  - item: Item ID (e.g., diamond_sword)
  - amount: Number of items
  - nbt: Optional NBT data

### Teleport Command
- Parameters:
  - player: Target player name
  - x: X coordinate
  - y: Y coordinate
  - z: Z coordinate

### Gamemode Command
- Parameters:
  - player: Target player name
  - mode: Game mode (survival, creative, adventure, spectator)

### Effect Command
- Parameters:
  - player: Target player name
  - effect: Effect ID
  - duration: Effect duration in seconds
  - amplifier: Effect level (0-based)

## Contributing

Feel free to submit issues and enhancement requests! 