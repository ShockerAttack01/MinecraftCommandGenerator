# Command Generation and Validation System

## Overview
The command generation system is responsible for creating valid Minecraft `/give` commands based on user input, providing real-time validation and feedback. This document details how commands are generated, validated, and how feedback is provided to users.

## Command Structure

### Basic Format
```
/give <player> <item> [amount] [nbt]
```

### Components
1. **Command Type**: Always "give"
2. **Player**: Target player or selector
3. **Item**: Minecraft item ID
4. **Amount**: Optional quantity (default: 1)
5. **NBT**: Optional NBT data

## Command Generation

### 1. Parameter Collection
```python
def update_command(self):
    command_parts = [self.command_type]
    
    # Add player parameter
    player = self.get_parameter_value("player")
    if player:
        command_parts.append(player)
    
    # Add item parameter
    if "raw_item" in self.parameter_vars:
        command_parts.append(self.parameter_vars["raw_item"])
    else:
        item = self.get_parameter_value("item")
        if item:
            command_parts.append(item.lower().replace(" ", "_"))
    
    # Add amount parameter
    amount = self.get_parameter_value("amount")
    if amount and amount != "1":
        command_parts.append(amount)
    
    # Add NBT parameter
    nbt = self.get_parameter_value("nbt")
    if nbt:
        command_parts.append(nbt)
    
    return " ".join(command_parts)
```

### 2. Parameter Processing
- **Player**: Validates against target selectors or player name rules
- **Item**: Converts display names to item IDs
- **Amount**: Ensures numeric value
- **NBT**: Passes through without modification

## Validation System

### 1. Basic Validation
```python
# Check command completeness
if len(command_parts) < 3:
    feedback.append("⚠️ Command is incomplete. Please fill in player and item.")
    return feedback
```

### 2. Player Validation
```python
# Validate player name or selector
if not (player in TARGET_SELECTORS or re.match(r"^[a-zA-Z0-9_]{1,16}$", player)):
    feedback.append("⚠️ Invalid player/target selector.")
```

### 3. Item Validation
```python
# Validate item ID format
if not re.match(r"^[a-z0-9_]+$", item_id):
    feedback.append("⚠️ Invalid item ID.")
```

### 4. Amount Validation
```python
# Validate amount is numeric
if len(command_parts) > 3 and not command_parts[3].isdigit():
    feedback.append("⚠️ Amount must be a number.")
```

## Feedback System

### 1. Feedback Types
- Command description
- Parameter validation
- Item category information
- Command validity status
- Error messages

### 2. Feedback Generation
```python
def get_feedback(self) -> List[str]:
    feedback = []
    
    # Add command description
    feedback.append(f"📝 {self.command_data['description']}")
    
    # Add validation feedback
    if not self.is_valid():
        feedback.append("⚠️ Command is invalid.")
    
    # Add parameter feedback
    for param in self.command_data["parameters"]:
        if param in self.command_data["feedback"]:
            feedback.append(f"• {param}: {self.command_data['feedback'][param]}")
    
    return feedback
```

### 3. Feedback Categories
- **Info**: General command information
- **Warning**: Validation issues
- **Error**: Critical problems
- **Success**: Command is valid

## Real-time Updates

### 1. Update Triggers
- Parameter changes
- Category changes
- Item selection
- Amount changes
- NBT input

### 2. Update Process
1. Collect current parameter values
2. Generate command string
3. Validate command
4. Generate feedback
5. Update UI

## Error Handling

### 1. Invalid Inputs
- Empty required fields
- Invalid player names
- Unknown item IDs
- Non-numeric amounts
- Malformed NBT data

### 2. Edge Cases
- Missing parameters
- Invalid selectors
- Unknown items
- Zero amounts
- Special characters

## Command Execution

### 1. Pre-execution Checks
- Command validity
- Parameter completeness
- Value ranges
- Format correctness

### 2. Execution Process
1. Validate command
2. Check permissions
3. Execute command
4. Handle response
5. Update feedback

## Future Improvements

### 1. Enhanced Validation
- More detailed error messages
- Parameter-specific validation
- NBT syntax checking
- Command preview

### 2. Additional Features
- Command history
- Favorite commands
- Command templates
- Batch commands
- Command scheduling 