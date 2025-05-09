from command_summarizer import CommandSummarizer

# Minecraft item and effect data

# Target selectors
TARGET_SELECTORS = ["@a", "@p", "@e", "@r", "@s"]

# Minecraft versions
VERSIONS = [
    "1.20.4", "1.20.2", "1.20.1", "1.20",
    "1.19.4", "1.19.3", "1.19.2", "1.19.1", "1.19",
    "1.18.2", "1.18.1", "1.18",
    "1.17.1", "1.17",
    "1.16.5", "1.16.4", "1.16.3", "1.16.2", "1.16.1", "1.16"
]

# Effect categories and effects
EFFECT_CATEGORIES = {
    "Positive Effects": {
        "speed": "Speed",
        "haste": "Haste",
        "strength": "Strength",
        "instant_health": "Instant Health",
        "jump_boost": "Jump Boost",
        "regeneration": "Regeneration",
        "resistance": "Resistance",
        "fire_resistance": "Fire Resistance",
        "water_breathing": "Water Breathing",
        "invisibility": "Invisibility",
        "night_vision": "Night Vision",
        "health_boost": "Health Boost",
        "absorption": "Absorption",
        "saturation": "Saturation",
        "luck": "Luck",
        "slow_falling": "Slow Falling",
        "conduit_power": "Conduit Power",
        "dolphins_grace": "Dolphin's Grace",
        "hero_of_the_village": "Hero of the Village"
    },
    "Negative Effects": {
        "slowness": "Slowness",
        "mining_fatigue": "Mining Fatigue",
        "instant_damage": "Instant Damage",
        "nausea": "Nausea",
        "blindness": "Blindness",
        "hunger": "Hunger",
        "weakness": "Weakness",
        "poison": "Poison",
        "wither": "Wither",
        "levitation": "Levitation",
        "unluck": "Bad Luck",
        "darkness": "Darkness",
        "glowing": "Glowing"
    }
}

# Item categories and items
ITEM_CATEGORIES = {
    "Tools": [
        "wooden_pickaxe", "stone_pickaxe", "iron_pickaxe", "golden_pickaxe", "diamond_pickaxe", "netherite_pickaxe",
        "wooden_axe", "stone_axe", "iron_axe", "golden_axe", "diamond_axe", "netherite_axe",
        "wooden_shovel", "stone_shovel", "iron_shovel", "golden_shovel", "diamond_shovel", "netherite_shovel",
        "wooden_hoe", "stone_hoe", "iron_hoe", "golden_hoe", "diamond_hoe", "netherite_hoe",
        "fishing_rod", "flint_and_steel", "shears", "brush", "spyglass", "compass", "recovery_compass",
        "clock", "name_tag", "lead", "saddle", "carrot_on_a_stick", "warped_fungus_on_a_stick"
    ],
    "Weapons": [
        "wooden_sword", "stone_sword", "iron_sword", "golden_sword", "diamond_sword", "netherite_sword",
        "bow", "crossbow", "trident", "shield", "totem_of_undying", "snowball", "egg", "ender_pearl",
        "splash_potion", "lingering_potion", "tipped_arrow", "spectral_arrow"
    ],
    "Armor": [
        "leather_helmet", "leather_chestplate", "leather_leggings", "leather_boots",
        "chainmail_helmet", "chainmail_chestplate", "chainmail_leggings", "chainmail_boots",
        "iron_helmet", "iron_chestplate", "iron_leggings", "iron_boots",
        "golden_helmet", "golden_chestplate", "golden_leggings", "golden_boots",
        "diamond_helmet", "diamond_chestplate", "diamond_leggings", "diamond_boots",
        "netherite_helmet", "netherite_chestplate", "netherite_leggings", "netherite_boots",
        "turtle_helmet", "elytra", "carved_pumpkin", "skull"
    ],
    "Blocks": [
        "stone", "dirt", "grass_block", "cobblestone", "oak_planks", "spruce_planks", "birch_planks", "jungle_planks",
        "acacia_planks", "dark_oak_planks", "mangrove_planks", "cherry_planks", "bamboo_planks",
        "oak_log", "spruce_log", "birch_log", "jungle_log", "acacia_log", "dark_oak_log", "mangrove_log", "cherry_log",
        "glass", "glass_pane", "white_wool", "orange_wool", "magenta_wool", "light_blue_wool", "yellow_wool", "lime_wool",
        "pink_wool", "gray_wool", "light_gray_wool", "cyan_wool", "purple_wool", "blue_wool", "brown_wool", "green_wool",
        "red_wool", "black_wool", "terracotta", "white_terracotta", "orange_terracotta", "magenta_terracotta",
        "light_blue_terracotta", "yellow_terracotta", "lime_terracotta", "pink_terracotta", "gray_terracotta",
        "light_gray_terracotta", "cyan_terracotta", "purple_terracotta", "blue_terracotta", "brown_terracotta",
        "green_terracotta", "red_terracotta", "black_terracotta", "concrete", "white_concrete", "orange_concrete",
        "magenta_concrete", "light_blue_concrete", "yellow_concrete", "lime_concrete", "pink_concrete", "gray_concrete",
        "light_gray_concrete", "cyan_concrete", "purple_concrete", "blue_concrete", "brown_concrete", "green_concrete",
        "red_concrete", "black_concrete", "glazed_terracotta", "white_glazed_terracotta", "orange_glazed_terracotta",
        "magenta_glazed_terracotta", "light_blue_glazed_terracotta", "yellow_glazed_terracotta", "lime_glazed_terracotta",
        "pink_glazed_terracotta", "gray_glazed_terracotta", "light_gray_glazed_terracotta", "cyan_glazed_terracotta",
        "purple_glazed_terracotta", "blue_glazed_terracotta", "brown_glazed_terracotta", "green_glazed_terracotta",
        "red_glazed_terracotta", "black_glazed_terracotta"
    ],
    "Ores & Minerals": [
        "coal", "iron_ingot", "gold_ingot", "diamond", "emerald", "lapis_lazuli", "redstone", "netherite_ingot",
        "coal_ore", "iron_ore", "gold_ore", "diamond_ore", "emerald_ore", "lapis_ore", "redstone_ore",
        "nether_gold_ore", "nether_quartz_ore", "ancient_debris", "deepslate_coal_ore", "deepslate_iron_ore",
        "deepslate_gold_ore", "deepslate_diamond_ore", "deepslate_emerald_ore", "deepslate_lapis_ore",
        "deepslate_redstone_ore", "copper_ore", "deepslate_copper_ore", "copper_ingot", "raw_copper",
        "raw_iron", "raw_gold", "amethyst_shard", "amethyst_block", "budding_amethyst", "calcite", "tuff"
    ],
    "Food": [
        "apple", "bread", "cooked_beef", "cooked_chicken", "cooked_porkchop", "cooked_mutton", "cooked_rabbit",
        "golden_apple", "enchanted_golden_apple", "carrot", "potato", "baked_potato", "beetroot", "melon_slice",
        "sweet_berries", "glow_berries", "chorus_fruit", "cooked_cod", "cooked_salmon", "tropical_fish",
        "pufferfish", "cookie", "cake", "pumpkin_pie", "honey_bottle", "mushroom_stew", "rabbit_stew",
        "beetroot_soup", "suspicious_stew", "dried_kelp", "cooked_egg", "rotten_flesh", "spider_eye",
        "fermented_spider_eye", "poisonous_potato", "dried_kelp_block"
    ],
    "Special Items": [
        "ender_pearl", "ender_eye", "blaze_rod", "blaze_powder", "ghast_tear", "magma_cream", "slime_ball",
        "gunpowder", "string", "feather", "leather", "rabbit_hide", "scute", "prismarine_shard",
        "prismarine_crystals", "heart_of_the_sea", "nautilus_shell", "sculk", "echo_shard", "nether_star",
        "dragon_egg", "dragon_breath", "elytra", "trident", "totem_of_undying", "wither_skeleton_skull",
        "player_head", "zombie_head", "skeleton_skull", "creeper_head", "dragon_head", "music_disc_13",
        "music_disc_cat", "music_disc_blocks", "music_disc_chirp", "music_disc_far", "music_disc_mall",
        "music_disc_mellohi", "music_disc_stal", "music_disc_strad", "music_disc_ward", "music_disc_11",
        "music_disc_wait", "music_disc_pigstep", "music_disc_otherside", "music_disc_5", "music_disc_relic"
    ],
    "Command Blocks": [
        "command_block", "chain_command_block", "repeating_command_block", "structure_block",
        "structure_void", "barrier", "light", "jigsaw", "debug_stick", "knowledge_book",
        "written_book", "book_and_quill", "filled_map", "command_block_minecart"
    ],
    "Redstone": [
        "redstone", "redstone_block", "redstone_torch", "redstone_lamp", "repeater", "comparator",
        "observer", "dispenser", "dropper", "hopper", "piston", "sticky_piston", "slime_block",
        "honey_block", "target", "tripwire_hook", "tripwire", "daylight_detector", "sculk_sensor",
        "calibrated_sculk_sensor", "note_block", "powered_rail", "detector_rail", "activator_rail",
        "lever", "button", "pressure_plate", "weighted_pressure_plate"
    ],
    "Transportation": [
        "minecart", "chest_minecart", "furnace_minecart", "hopper_minecart", "tnt_minecart",
        "command_block_minecart", "boat", "oak_boat", "spruce_boat", "birch_boat", "jungle_boat",
        "acacia_boat", "dark_oak_boat", "mangrove_boat", "cherry_boat", "bamboo_raft"
    ],
    "Brewing": [
        "brewing_stand", "cauldron", "water_cauldron", "lava_cauldron", "powder_snow_cauldron",
        "glass_bottle", "potion", "splash_potion", "lingering_potion", "tipped_arrow",
        "fermented_spider_eye", "spider_eye", "blaze_powder", "magma_cream", "ghast_tear",
        "rabbit_foot", "glistering_melon_slice", "golden_carrot", "pufferfish", "turtle_helmet",
        "phantom_membrane", "dragon_breath", "nether_wart", "glowstone_dust"
    ],
    "Decoration": [
        "painting", "item_frame", "glow_item_frame", "armor_stand", "banner", "white_banner",
        "orange_banner", "magenta_banner", "light_blue_banner", "yellow_banner", "lime_banner",
        "pink_banner", "gray_banner", "light_gray_banner", "cyan_banner", "purple_banner",
        "blue_banner", "brown_banner", "green_banner", "red_banner", "black_banner",
        "flower_pot", "bell", "lantern", "soul_lantern", "campfire", "soul_campfire",
        "end_rod", "sea_pickle", "conduit", "beacon", "end_crystal"
    ]
}

# Command types and their parameters
COMMAND_TYPES = {
    "give": {
        "parameters": ["player", "item", "amount", "nbt"],
        "description": "Gives a specified number of items to a player or entity. The items can be customized with NBT data for special properties.",
        "summary": lambda p: CommandSummarizer.summarize("give", p),
        "feedback": {
            "player": "Target player or entity to receive the item",
            "item": "The item to give (use the search box to find items)",
            "amount": "Number of items to give (optional, defaults to 1)",
            "nbt": "NBT data for the item (optional, for advanced users)"
        }
    },
    "tp": {
        "parameters": ["player", "x", "y", "z"],
        "description": "Teleports a player or entity to specific coordinates or to another entity. Can include rotation (yaw and pitch) for precise positioning.",
        "summary": lambda p: CommandSummarizer.summarize("tp", p),
        "feedback": {
            "player": "Target player to teleport",
            "x": "X coordinate (can use ~ for relative position)",
            "y": "Y coordinate (can use ~ for relative position)",
            "z": "Z coordinate (can use ~ for relative position)"
        },
        "presets": {
            "x": ["~", "~0", "~1", "~-1"],
            "y": ["~", "~0", "~1", "~-1"],
            "z": ["~", "~0", "~1", "~-1"]
        }
    },
    "gamemode": {
        "parameters": ["player", "mode"],
        "description": "Changes a player's game mode to survival, creative, adventure, or spectator. Each mode has different abilities and restrictions.",
        "summary": lambda p: CommandSummarizer.summarize("gamemode", p),
        "feedback": {
            "player": "Target player to change game mode",
            "mode": "Game mode (survival, creative, adventure, spectator)"
        },
        "presets": {
            "mode": ["survival", "creative", "adventure", "spectator"]
        }
    },
    "effect": {
        "parameters": ["player", "effect", "duration", "amplifier", "hide_particles"],
        "description": "Applies a status effect to a player or entity for a specified duration and level. Effects can be beneficial or harmful, and particles can be hidden.",
        "summary": lambda p: CommandSummarizer.summarize("effect", p),
        "feedback": {
            "player": "Target player or entity to receive the effect",
            "effect": "The effect to apply (use the search box to find effects)",
            "duration": "How long the effect lasts in seconds",
            "amplifier": "Effect level (0-based, higher means stronger effect)",
            "hide_particles": "Whether to hide the effect particles (true/false)"
        }
    },
    "time": {
        "parameters": ["action", "value"],
        "description": "Changes or queries the world's game time",
        "summary": lambda p: CommandSummarizer.summarize("time", p),
        "feedback": {
            "action": "Command action (set, add, query)",
            "value": "Time value (day, night, noon, midnight, or number of ticks)"
        },
        "presets": {
            "action": ["set", "add", "query"],
            "value": ["day", "night", "noon", "midnight", "0", "1000", "6000", "12000", "18000"]
        }
    },
    "weather": {
        "parameters": ["type", "duration"],
        "description": "Changes the weather",
        "summary": lambda p: CommandSummarizer.summarize("weather", p),
        "feedback": {
            "type": "Weather type (clear, rain, thunder)",
            "duration": "Duration in seconds (optional)"
        },
        "presets": {
            "type": ["clear", "rain", "thunder"],
            "duration": ["60", "300", "600", "1800", "3600"]
        }
    },
    "difficulty": {
        "parameters": ["level"],
        "description": "Sets the game difficulty",
        "summary": lambda p: CommandSummarizer.summarize("difficulty", p),
        "feedback": {
            "level": "Difficulty level (peaceful, easy, normal, hard)"
        },
        "presets": {
            "level": ["peaceful", "easy", "normal", "hard"]
        }
    },
    "gamerule": {
        "parameters": ["rule", "value"],
        "description": "Changes a game rule",
        "summary": lambda p: CommandSummarizer.summarize("gamerule", p),
        "feedback": {
            "rule": "Game rule to change (e.g., keepInventory, doDaylightCycle)",
            "value": "New value (true/false)"
        },
        "presets": {
            "rule": [
                "keepInventory", "doDaylightCycle", "doMobSpawning", "doWeatherCycle",
                "mobGriefing", "naturalRegeneration", "doFireTick", "doInsomnia",
                "doImmediateRespawn", "doLimitedCrafting", "doTileDrops",
                "doEntityDrops", "commandBlockOutput", "logAdminCommands",
                "showDeathMessages", "randomTickSpeed", "sendCommandFeedback",
                "reducedDebugInfo", "spectatorsGenerateChunks", "spawnRadius",
                "disableElytraMovementCheck", "disableRaids", "doPatrolSpawning",
                "doTraderSpawning", "doWardenSpawning", "fallDamage", "fireDamage",
                "drowningDamage", "freezeDamage", "forgiveDeadPlayers",
                "universalAnger", "playersSleepingPercentage"
            ],
            "value": ["true", "false"]
        }
    },
    "enchant": {
        "parameters": ["player", "enchantment", "level"],
        "description": "Enchants a player's held item",
        "summary": lambda p: CommandSummarizer.summarize("enchant", p),
        "feedback": {
            "player": "Target player",
            "enchantment": "Enchantment ID (e.g., sharpness, protection)",
            "level": "Enchantment level (optional, defaults to 1)"
        },
        "presets": {
            "enchantment": [
                "sharpness", "protection", "efficiency", "unbreaking", "fortune",
                "looting", "power", "punch", "flame", "infinity", "luck_of_the_sea",
                "lure", "frost_walker", "depth_strider", "aqua_affinity",
                "respiration", "thorns", "feather_falling", "blast_protection",
                "projectile_protection", "fire_protection", "smite", "bane_of_arthropods",
                "knockback", "fire_aspect", "sweeping", "channeling", "impaling",
                "loyalty", "riptide", "multishot", "quick_charge", "piercing",
                "mending", "vanishing_curse", "binding_curse", "soul_speed",
                "swift_sneak"
            ],
            "level": ["1", "2", "3", "4", "5"]
        }
    },
    "kill": {
        "parameters": ["target"],
        "description": "Kills entities",
        "summary": lambda p: CommandSummarizer.summarize("kill", p),
        "feedback": {
            "target": "Target selector or player name (optional, defaults to @s)"
        }
    },
    "clear": {
        "parameters": ["player", "item", "amount"],
        "description": "Clears items from a player's inventory",
        "summary": lambda p: CommandSummarizer.summarize("clear", p),
        "feedback": {
            "player": "Target player (optional, defaults to @s)",
            "item": "Item to clear (optional)",
            "amount": "Amount to clear (optional)"
        }
    },
    "fill": {
        "parameters": ["x1", "y1", "z1", "x2", "y2", "z2", "block"],
        "description": "Fills a region with blocks",
        "summary": lambda p: CommandSummarizer.summarize("fill", p),
        "feedback": {
            "x1": "First X coordinate",
            "y1": "First Y coordinate",
            "z1": "First Z coordinate",
            "x2": "Second X coordinate",
            "y2": "Second Y coordinate",
            "z2": "Second Z coordinate",
            "block": "Block to fill with"
        },
        "presets": {
            "x1": ["~", "~0", "~1", "~-1"],
            "y1": ["~", "~0", "~1", "~-1"],
            "z1": ["~", "~0", "~1", "~-1"],
            "x2": ["~", "~0", "~1", "~-1"],
            "y2": ["~", "~0", "~1", "~-1"],
            "z2": ["~", "~0", "~1", "~-1"]
        }
    }
} 