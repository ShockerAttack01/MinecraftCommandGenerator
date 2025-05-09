# Getting Started

Welcome to the Minecraft Command Generator! This guide will help you get started with the application.

## Prerequisites

- Python 3.8 or higher
- Git (for installation)
- Minecraft Java Edition (for testing commands)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShockerAttack01/MinecraftCommandGenerator.git
   cd MinecraftCommandGenerator
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the application:
   ```bash
   python main.py
   ```

2. The main window will open with:
   - Command type selection
   - Parameter input fields
   - Real-time validation
   - Command preview

## Basic Usage

### Creating Your First Command

1. Select a command type from the dropdown
2. Fill in the required parameters
3. Watch the command preview update in real-time
4. Copy the generated command

### Using Item Search

1. Click the item search field
2. Type to search for items
3. Use categories to filter results
4. Select an item from the suggestions

### Command Validation

- Required fields are marked with *
- Invalid inputs are highlighted in red
- Hover over fields for help text
- Check the command preview for errors

## Common Tasks

### Giving Items
1. Select "Give Command"
2. Choose a player
3. Search for an item
4. Set quantity and NBT data
5. Copy the command

### Applying Effects
1. Select "Effect Command"
2. Choose a player
3. Select an effect
4. Set duration and amplifier
5. Copy the command

## Troubleshooting

### Common Issues

1. **Application won't start**
   - Check Python version
   - Verify virtual environment
   - Check dependencies

2. **Item search not working**
   - Check internet connection
   - Verify item data files
   - Clear search cache

3. **Command validation errors**
   - Check parameter types
   - Verify player names
   - Check item IDs

## Next Steps

- Read the [[Basic Usage]] guide
- Explore [[Command Types]]
- Learn about [[Item Search]]
- Check [[Troubleshooting]] for help

## Support

- Visit our [GitHub Issues](https://github.com/ShockerAttack01/MinecraftCommandGenerator/issues)
- Join our [Discord Community](https://discord.gg/your-invite-link)
- Check the [[Troubleshooting]] guide 