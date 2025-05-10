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
