"""
Minecraft Data Module

This module contains data for Minecraft commands, items, effects, and versions.
It also provides helper functions for handling enchantments, attributes, effects, and items.
"""

from .versions import VERSIONS, VERSION_NUMBERS
from .items import ITEM_CATEGORIES, ITEM_TAGS, ITEM_VERSIONS
from .effects import EFFECT_CATEGORIES
from .blocks import BLOCK_VERSIONS
from .commands import COMMAND_TYPES
from .enchantments import ENCHANTMENTS
from .attributes import ATTRIBUTES

# Target selectors
TARGET_SELECTORS = ["@a", "@p", "@e", "@r", "@s"]

def get_enchantment_options() -> list:
    """
    Get a list of all available enchantments.

    Returns:
        list: A list of enchantment IDs.
    """
    return ENCHANTMENTS

def get_attribute_options() -> list:
    """
    Get a list of all available attributes.

    Returns:
        list: A list of attribute IDs.
    """
    return ATTRIBUTES

def get_effect_categories() -> dict:
    """
    Get all effect categories and their effects.

    Returns:
        dict: A dictionary of effect categories and their effects.
    """
    return EFFECT_CATEGORIES

def get_item_categories() -> dict:
    """
    Get all item categories and their items.

    Returns:
        dict: A dictionary of item categories and their items.
    """
    return ITEM_CATEGORIES

def get_item_tags() -> dict:
    """
    Get all item tags.

    Returns:
        dict: A dictionary of item tags.
    """
    return ITEM_TAGS

def get_versioned_items(version: str) -> list:
    """
    Get a list of items available in a specific Minecraft version.

    Args:
        version (str): The Minecraft version.

    Returns:
        list: A list of items available in the specified version.
    """
    return [item for item, item_version in ITEM_VERSIONS.items() if compare_versions(item_version, version) <= 0]

def compare_versions(version1: str, version2: str) -> int:
    """
    Compare two version strings.

    Args:
        version1 (str): The first version string.
        version2 (str): The second version string.

    Returns:
        int: 1 if version1 > version2, -1 if version1 < version2, 0 if equal.
    """
    v1_parts = [int(x) for x in version1.split('.')]
    v2_parts = [int(x) for x in version2.split('.')]
    for i in range(max(len(v1_parts), len(v2_parts))):
        v1 = v1_parts[i] if i < len(v1_parts) else 0
        v2 = v2_parts[i] if i < len(v2_parts) else 0
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
    return 0

def get_item_data(all_formatted_items: list) -> list:
    """
    Generate item data with tags and versions.

    Args:
        all_formatted_items (list): List of all formatted item names.

    Returns:
        list: A list of dictionaries containing item data.
    """
    category_items = set(item for items in ITEM_CATEGORIES.values() for item in items)
    all_items = list(category_items)
    all_formatted_items = [item.replace("_", " ").title() for item in all_items]

    for item in all_formatted_items:
        raw_item = item.lower().replace(" ", "_")
        if raw_item not in category_items:
            all_items.append(raw_item)
            all_formatted_items.append(item)

    item_data = [
        {
            'formatted': formatted_item,
            'raw': raw_item,
            'tags': ITEM_TAGS.get(raw_item, set()) | set(raw_item.split('_')) | set(formatted_item.lower().split()),
            'version': ITEM_VERSIONS.get(raw_item, "1.0")
        }
        for formatted_item, raw_item in zip(all_formatted_items, all_items)
    ]
    item_data.sort(key=lambda x: x['formatted'])
    return item_data
