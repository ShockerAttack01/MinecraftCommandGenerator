# Item Search System Documentation

## Overview
The item search system provides a powerful and user-friendly way to find and select Minecraft items. It combines category filtering, real-time search, and suggestion display to help users quickly find the items they need.

## Data Structure

### Item Storage
```python
# Item data is stored in two parallel lists:
self.all_items = []        # Raw item IDs (e.g., "diamond_sword")
self.all_formatted_items = []  # Display names (e.g., "Diamond Sword")
```

### Categories
```python
self.item_categories = {
    "Combat": ["diamond_sword", "bow", ...],
    "Building": ["stone", "oak_planks", ...],
    # ... more categories
}
```

## Search Process

### 1. Initialization
```python
# During initialization:
1. Collect all items from categories
2. Add any additional items from all_formatted_items
3. Sort items alphabetically
4. Create parallel lists for raw IDs and display names
```

### 2. Category Filtering
```python
# When category changes:
1. Clear current selection
2. Update suggestions based on new category
3. If "All Categories" selected:
   - Show all items
4. If specific category selected:
   - Show only items from that category
```

### 3. Search Filtering
```python
# When user types:
1. Get current search text
2. Filter items based on:
   - Selected category
   - Search text (case-insensitive)
   - Matches against both display names and item IDs
3. Show up to 10 matching items
```

## Suggestion Display

### 1. Suggestion Frame
```python
# Components:
- Scrollable frame
- Height: 150 pixels
- Shows up to 10 items
- Each item is a clickable button
```

### 2. Item Buttons
```python
# Each button:
- Shows formatted item name
- Triggers on_item_selected when clicked
- Passes both formatted name and raw ID
```

## Event Handling

### 1. Category Change
```python
def on_category_change(self, category: str):
    # Clear current selection
    self.parameter_vars["item"].delete(0, "end")
    if "raw_item" in self.parameter_vars:
        del self.parameter_vars["raw_item"]
    
    # Update suggestions
    self.update_suggestions()
    self.on_parameter_change()
```

### 2. Search Input
```python
def on_item_search(self, event):
    # Get search text
    search_text = self.parameter_vars["item"].get().lower()
    
    # Update suggestions
    self.update_suggestions(search_text)
    self.on_parameter_change()
```

### 3. Item Selection
```python
def on_item_selected(self, formatted_item: str, raw_item: str):
    # Update search box
    self.parameter_vars["item"].delete(0, "end")
    self.parameter_vars["item"].insert(0, formatted_item)
    
    # Store raw item ID
    self.parameter_vars["raw_item"] = raw_item
    
    # Update suggestions
    self.update_suggestions()
    self.on_parameter_change()
```

## Search Algorithm

### 1. Item Matching
```python
# For each item:
if not search_text or search_text in formatted_item.lower() or search_text in raw_item:
    matches.append((formatted_item, raw_item))
```

### 2. Category Filtering
```python
# If category selected:
category_items = self.item_categories[selected_category]
formatted_items = [item.replace("_", " ").title() for item in category_items]
sorted_pairs = sorted(zip(formatted_items, category_items))
items_to_show = sorted_pairs
```

## Performance Considerations

### 1. Optimization
- Items are pre-sorted
- Search is case-insensitive
- Limited to 10 suggestions
- Uses parallel lists for quick access

### 2. Memory Usage
- Stores both raw IDs and formatted names
- Maintains category structure
- Cleans up old suggestions

### 3. Real-time Updates
- Updates on every keystroke
- Maintains smooth performance
- Clears old suggestions efficiently

## Error Handling

### 1. Invalid Inputs
- Handles empty search text
- Manages invalid categories
- Deals with missing items

### 2. Edge Cases
- Empty categories
- Special characters in search
- Very long item names
- Missing raw IDs

## Future Improvements

### 1. Potential Enhancements
- Fuzzy search matching
- Item icons
- Item descriptions
- Recent items list
- Favorite items

### 2. Performance Optimizations
- Caching search results
- Lazy loading of suggestions
- Background search processing
- Search result pagination 