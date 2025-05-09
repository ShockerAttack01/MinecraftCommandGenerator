# Getting Started

Welcome to the Minecraft Command Generator! This guide will help you get started with using the tool.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShockerAttack01/MinecraftCommandGenerator.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Basic Usage

### 1. Selecting a Command
- Choose a command type from the dropdown menu
- Available commands include:
  - `/give`: Give items to players
  - `/effect`: Apply effects to players
  - `/gamemode`: Change player gamemode
  - `/teleport`: Teleport players

### 2. Using the Give Command
1. Select a player:
   - Enter a player name
   - Or use a target selector (@a, @p, @e, @r, @s)

2. Choose an item:
   - Use the category dropdown to filter items
   - Search for items by name
   - Select from the suggestions

3. Set the amount:
   - Enter a number (default: 1)
   - Leave empty for default amount

4. Add NBT data (optional):
   - Enter NBT data if needed
   - Format: `{key:value}`

### 3. Command Feedback
- The command is validated in real-time
- Feedback shows:
  - Command validity
  - Parameter status
  - Error messages
  - Item information

## Documentation

### Wiki Updates
The project's documentation is automatically updated through GitHub Actions:
- Documentation is stored in the `docs/wiki` directory
- Changes are automatically validated and formatted
- Updates are pushed to the GitHub wiki
- Broken links and formatting issues are caught early

### Contributing to Documentation
1. Make changes to files in `docs/wiki`
2. Commit and push your changes
3. The wiki will be automatically updated
4. Check the Actions tab for validation results

## Next Steps

- Read the [[Basic Usage]] guide for more details
- Check out the [[Item Search Guide]] for advanced item selection
- Visit [[Troubleshooting]] if you encounter any issues

## Tips

- Use the category filter to quickly find items
- Target selectors can save time when affecting multiple players
- The feedback system helps prevent invalid commands
- NBT data is optional but useful for custom items 