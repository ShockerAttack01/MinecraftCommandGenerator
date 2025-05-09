# UI Components Documentation

## Overview
The GiveCommand interface consists of several UI components that work together to provide a user-friendly command generation experience. This document details each component and its functionality.

## Component Hierarchy

```
GiveCommand
├── Player Input Frame
│   ├── Label
│   ├── Entry Field
│   └── Target Selector Dropdown
├── Item Search Frame
│   ├── Label
│   ├── Category Dropdown
│   ├── Search Entry
│   └── Suggestions Frame
├── Amount Input Frame
│   ├── Label
│   └── Entry Field
└── NBT Input Frame
    ├── Label
    └── Entry Field
```

## Detailed Component Descriptions

### 1. Player Input Frame
**Purpose**: Handles player/target selection for the command.

**Components**:
- **Label**: "Player:" text indicator
- **Entry Field**: 
  - For manual player name input
  - Validates player names in real-time
  - Supports alphanumeric characters and underscores
- **Target Selector Dropdown**:
  - Options: @a, @p, @e, @r, @s
  - Automatically fills entry field when selected
  - Provides quick access to common selectors

### 2. Item Search Frame
**Purpose**: Manages item selection with search and category filtering.

**Components**:
- **Label**: "Item:" text indicator
- **Category Dropdown**:
  - Shows "All Categories" by default
  - Lists all available item categories
  - Sorted alphabetically
  - Filters items when changed
- **Search Entry**:
  - Real-time search functionality
  - Case-insensitive matching
  - Matches against both display names and item IDs
- **Suggestions Frame**:
  - Scrollable frame for item suggestions
  - Shows up to 10 matching items
  - Each item is a clickable button
  - Updates in real-time as user types

### 3. Amount Input Frame
**Purpose**: Specifies the quantity of items to give.

**Components**:
- **Label**: "Amount:" text indicator
- **Entry Field**:
  - Default value: 1
  - Numeric validation
  - Optional parameter
  - Real-time validation

### 4. NBT Input Frame
**Purpose**: Handles NBT data input for items.

**Components**:
- **Label**: "NBT:" text indicator
- **Entry Field**:
  - Optional parameter
  - Raw NBT string input
  - No validation (passed through as-is)

## UI Behavior

### 1. Real-time Updates
- All components update in real-time as user interacts
- Command string updates immediately
- Feedback updates with each change
- Suggestions refresh as user types

### 2. Validation
- Player names validated against Minecraft rules
- Amount must be numeric
- Item IDs must be valid Minecraft items
- NBT data passed through without validation

### 3. Error Handling
- Invalid inputs show warning messages
- Suggestions help prevent invalid item selection
- Clear feedback on command validity
- Visual indicators for required fields

### 4. Accessibility
- Clear labels for all inputs
- Consistent layout
- Intuitive interaction flow
- Helpful feedback messages

## Styling
- Uses CustomTkinter for modern look
- Consistent padding and spacing
- Clear visual hierarchy
- Responsive layout

## Event Handling
Each component triggers appropriate events:
1. Player input: Updates command and validates
2. Category change: Updates suggestions and command
3. Item search: Updates suggestions in real-time
4. Item selection: Updates command and feedback
5. Amount change: Updates command and validates
6. NBT input: Updates command string 