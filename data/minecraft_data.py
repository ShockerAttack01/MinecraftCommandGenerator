"""
Minecraft Data Module

This module contains data for Minecraft commands, items, effects, and versions.
"""

from .versions import VERSIONS, VERSION_NUMBERS
from .items import ITEM_CATEGORIES, ITEM_TAGS, ITEM_VERSIONS
from .effects import EFFECT_CATEGORIES
from .blocks import BLOCK_VERSIONS
from .commands import COMMAND_TYPES
from .enchantments import ENCHANTMENTS
from .attributes import ATTRIBUTES  # Import attributes

# Target selectors
TARGET_SELECTORS = ["@a", "@p", "@e", "@r", "@s"]
