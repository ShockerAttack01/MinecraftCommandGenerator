"""
Minecraft Data Module

This module contains data for Minecraft commands, items, effects, and versions.
"""

from command_summarizer import CommandSummarizer

# Minecraft item and effect data

# Target selectors
TARGET_SELECTORS = ["@a", "@p", "@e", "@r", "@s"]

# Minecraft versions
VERSIONS = [
    "1.20.4", "1.20.3", "1.20.2", "1.20.1", "1.20",
    "1.19.4", "1.19.3", "1.19.2", "1.19.1", "1.19",
    "1.18.2", "1.18.1", "1.18",
    "1.17.1", "1.17",
    "1.16.5", "1.16.4", "1.16.3", "1.16.2", "1.16.1", "1.16",
    "1.15.2", "1.15.1", "1.15",
    "1.14.4", "1.14.3", "1.14.2", "1.14.1", "1.14",
    "1.13.2", "1.13.1", "1.13",
    "1.12.2", "1.12.1", "1.12",
    "1.11.2", "1.11.1", "1.11",
    "1.10.2", "1.10.1", "1.10",
    "1.9.4", "1.9.3", "1.9.2", "1.9.1", "1.9",
    "1.8.9", "1.8.8", "1.8.7", "1.8.6", "1.8.5", "1.8.4", "1.8.3", "1.8.2", "1.8.1", "1.8",
    "1.7.10", "1.7.9", "1.7.8", "1.7.7", "1.7.6", "1.7.5", "1.7.4", "1.7.3", "1.7.2",
    "1.6.4", "1.6.3", "1.6.2", "1.6.1",
    "1.5.2", "1.5.1",
    "1.4.7", "1.4.6", "1.4.5", "1.4.4", "1.4.3", "1.4.2",
    "1.3.2", "1.3.1",
    "1.2.5", "1.2.4", "1.2.3", "1.2.2", "1.2.1",
    "1.1",
    "1.0.0"
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
    "Placeable Items": [
        "acacia_boat", "acacia_boat_with_chest", "armor_stand", "bamboo_raft", "bamboo_raft_with_chest",
        "beetroot_seeds", "birch_boat", "birch_boat_with_chest", "blue_egg", "bottle_o_enchanting",
        "bow", "brown_egg", "bucket", "bucket_of_axolotl", "bucket_of_cod", "bucket_of_pufferfish",
        "bucket_of_salmon", "bucket_of_tadpole", "bucket_of_tropical_fish", "carrot", "cherry_boat",
        "cherry_boat_with_chest", "cocoa_beans", "crossbow", "dark_oak_boat", "dark_oak_boat_with_chest",
        "egg", "end_crystal", "ender_pearl", "eye_of_ender", "fire_charge", "firework_rocket",
        "fishing_rod", "flint_and_steel", "glow_berries", "glow_item_frame", "item_frame",
        "jungle_boat", "jungle_boat_with_chest", "kelp", "lava_bucket", "lead", "lingering_potion",
        "mangrove_boat", "mangrove_boat_with_chest", "melon_seeds", "minecart", "minecart_with_chest",
        "minecart_with_command_block", "minecart_with_furnace", "minecart_with_hopper",
        "minecart_with_tnt", "nether_wart", "oak_boat", "oak_boat_with_chest", "painting",
        "pale_oak_boat", "pale_oak_boat_with_chest", "pitcher_pod", "potato", "powder_snow_bucket",
        "pumpkin_seeds", "redstone_dust", "snowball", "splash_potion", "spruce_boat",
        "spruce_boat_with_chest", "string", "sweet_berries", "torchflower_seeds", "trident",
        "water_bucket", "wheat_seeds", "wind_charge", "music_disc_creator_music_box"
    ],
    "Usable Items": [
        "amethyst_shard", "apple", "armadillo_scute", "arrow", "baked_potato", "beetroot",
        "beetroot_soup", "black_bundle", "black_dye", "blue_bundle", "blue_dye", "bone",
        "bone_meal", "book", "book_and_quill", "bowl", "bread", "brown_bundle", "brown_dye",
        "brush", "bundle", "carrot_on_a_stick", "chainmail_boots", "chainmail_chestplate",
        "chainmail_helmet", "chainmail_leggings", "charcoal", "chorus_fruit", "coal",
        "compass", "cooked_chicken", "cooked_cod", "cooked_mutton", "cooked_porkchop",
        "cooked_rabbit", "cooked_salmon", "cookie", "cyan_bundle", "cyan_dye", "debug_stick",
        "diamond_axe", "diamond_boots", "diamond_chestplate", "diamond_helmet", "diamond_hoe",
        "diamond_horse_armor", "diamond_leggings", "diamond_pickaxe", "diamond_shovel",
        "diamond_sword", "dried_kelp", "elytra", "empty_map", "enchanted_book",
        "enchanted_golden_apple", "glass_bottle", "glow_ink_sac", "goat_horn", "gold_ingot",
        "golden_apple", "golden_axe", "golden_boots", "golden_carrot", "golden_chestplate",
        "golden_helmet", "golden_hoe", "golden_horse_armor", "golden_leggings", "golden_pickaxe",
        "golden_shovel", "golden_sword", "gray_bundle", "gray_dye", "green_bundle", "green_dye",
        "honeycomb", "honey_bottle", "ink_sac", "iron_axe", "iron_boots", "iron_chestplate",
        "iron_helmet", "iron_hoe", "iron_horse_armor", "iron_ingot", "iron_leggings",
        "iron_pickaxe", "iron_shovel", "iron_sword", "knowledge_book", "lapis_lazuli",
        "leather_boots", "leather_cap", "leather_horse_armor", "leather_pants", "leather_tunic",
        "light_blue_bundle", "light_blue_dye", "light_gray_bundle", "light_gray_dye",
        "lime_bundle", "lime_dye", "mace", "magenta_bundle", "magenta_dye", "map",
        "explorer_map", "melon_slice", "milk_bucket", "mushroom_stew", "music_disc_5",
        "music_disc_11", "music_disc_13", "music_disc_blocks", "music_disc_cat",
        "music_disc_chirp", "music_disc_creator", "music_disc_far", "music_disc_mall",
        "music_disc_mellohi", "music_disc_otherside", "music_disc_pigstep",
        "music_disc_precipice", "music_disc_relic", "music_disc_stal", "music_disc_strad",
        "music_disc_wait", "music_disc_ward", "name_tag", "netherite_axe", "netherite_boots",
        "netherite_chestplate", "netherite_helmet", "netherite_hoe", "netherite_leggings",
        "netherite_pickaxe", "netherite_shovel", "netherite_sword", "ominous_bottle",
        "ominous_trial_key", "orange_bundle", "orange_dye", "pink_bundle", "pink_dye",
        "poisonous_potato", "pufferfish", "pumpkin_pie", "purple_bundle", "purple_dye",
        "rabbit_stew", "raw_beef", "raw_chicken", "raw_cod", "raw_mutton", "raw_porkchop",
        "raw_rabbit", "raw_salmon", "red_bundle", "red_dye", "rotten_flesh", "saddle",
        "shears", "shield", "slimeball", "spectral_arrow", "spider_eye", "spyglass",
        "steak", "stone_axe", "stone_hoe", "stone_pickaxe", "stone_shovel", "stone_sword",
        "sugar", "suspicious_stew", "tipped_arrow", "totem_of_undying", "trial_key",
        "tropical_fish", "turtle_shell", "warped_fungus_on_a_stick", "wheat",
        "white_bundle", "white_dye", "wolf_armor", "wooden_axe", "wooden_hoe",
        "wooden_pickaxe", "wooden_shovel", "wooden_sword", "written_book",
        "yellow_bundle", "yellow_dye", "music_disc_creator_music_box"
    ],
    "Crafting Materials": [
        "angler_pottery_sherd", "archer_pottery_sherd", "arms_up_pottery_sherd",
        "blade_pottery_sherd", "blaze_powder", "blaze_rod", "bolt_armor_trim",
        "bordure_indented_banner_pattern", "breeze_rod", "brewer_pottery_sherd",
        "brick", "burn_pottery_sherd", "charcoal", "clay_ball", "clock", "coal",
        "coast_armor_trim", "copper_ingot", "creeper_charge_banner_pattern",
        "danger_pottery_sherd", "diamond", "disc_fragment", "dragon_breath",
        "dune_armor_trim", "echo_shard", "emerald", "explorer_pottery_sherd",
        "eye_armor_trim", "feather", "fermented_spider_eye", "field_masoned_banner_pattern",
        "firework_star", "flint", "flow_armor_trim", "flow_banner_pattern",
        "flow_pottery_sherd", "flower_charge_banner_pattern", "friend_pottery_sherd",
        "ghast_tear", "glistering_melon_slice", "globe_banner_pattern",
        "glowstone_dust", "gold_nugget", "gunpowder", "guster_banner_pattern",
        "guster_pottery_sherd", "heart_of_the_sea", "heart_pottery_sherd",
        "heartbreak_pottery_sherd", "host_armor_trim", "howl_pottery_sherd",
        "iron_nugget", "lapis_lazuli", "leather", "lodestone_compass",
        "magma_cream", "miner_pottery_sherd", "mourner_pottery_sherd",
        "nautilus_shell", "nether_brick", "nether_quartz", "nether_star",
        "netherite_ingot", "netherite_scrap", "netherite_upgrade", "paper",
        "phantom_membrane", "plenty_pottery_sherd", "popped_chorus_fruit",
        "prismarine_crystals", "prismarine_shard", "prize_pottery_sherd",
        "rabbit_hide", "rabbit_foot", "raiser_armor_trim", "raw_copper",
        "raw_gold", "raw_iron", "recovery_compass", "resin_brick",
        "rib_armor_trim", "scrape_pottery_sherd", "sentry_armor_trim",
        "shaper_armor_trim", "sheaf_pottery_sherd", "shelter_pottery_sherd",
        "shulker_shell", "silence_armor_trim", "skull_charge_banner_pattern",
        "skull_pottery_sherd", "snort_pottery_sherd", "snout_armor_trim",
        "snout_banner_pattern", "spire_armor_trim", "stick", "thing_banner_pattern",
        "tide_armor_trim", "turtle_scute", "vex_armor_trim", "ward_armor_trim",
        "wayfinder_armor_trim", "wild_armor_trim"
    ],
    "Spawn Eggs": [
        "armadillo_spawn_egg", "allay_spawn_egg", "axolotl_spawn_egg",
        "bat_spawn_egg", "bee_spawn_egg", "blaze_spawn_egg", "bogged_spawn_egg",
        "breeze_spawn_egg", "camel_spawn_egg", "cat_spawn_egg",
        "cave_spider_spawn_egg", "chicken_spawn_egg", "cod_spawn_egg",
        "cow_spawn_egg", "creeper_spawn_egg", "creaking_spawn_egg",
        "dolphin_spawn_egg", "donkey_spawn_egg", "drowned_spawn_egg",
        "elder_guardian_spawn_egg", "ender_dragon_spawn_egg",
        "enderman_spawn_egg", "endermite_spawn_egg", "evoker_spawn_egg",
        "fox_spawn_egg", "frog_spawn_egg", "ghast_spawn_egg",
        "glow_squid_spawn_egg", "goat_spawn_egg", "guardian_spawn_egg",
        "happy_ghast_spawn_egg", "hoglin_spawn_egg", "horse_spawn_egg",
        "husk_spawn_egg", "iron_golem_spawn_egg", "llama_spawn_egg",
        "magma_cube_spawn_egg", "mooshroom_spawn_egg", "mule_spawn_egg",
        "npc_spawn_egg", "ocelot_spawn_egg", "panda_spawn_egg",
        "parrot_spawn_egg", "phantom_spawn_egg", "pig_spawn_egg",
        "piglin_spawn_egg", "piglin_brute_spawn_egg", "pillager_spawn_egg",
        "polar_bear_spawn_egg", "pufferfish_spawn_egg", "rabbit_spawn_egg",
        "ravager_spawn_egg", "salmon_spawn_egg", "sheep_spawn_egg",
        "shulker_spawn_egg", "silverfish_spawn_egg", "skeleton_horse_spawn_egg",
        "skeleton_spawn_egg", "slime_spawn_egg", "sniffer_spawn_egg",
        "snow_golem_spawn_egg", "spider_spawn_egg", "squid_spawn_egg",
        "stray_spawn_egg", "strider_spawn_egg", "tadpole_spawn_egg",
        "trader_llama_spawn_egg", "tropical_fish_spawn_egg",
        "turtle_spawn_egg", "vex_spawn_egg", "villager_spawn_egg",
        "vindicator_spawn_egg", "wandering_trader_spawn_egg",
        "warden_spawn_egg", "witch_spawn_egg", "wither_skeleton_spawn_egg",
        "wither_spawn_egg", "wolf_spawn_egg"
    ]
}

# Item tags for search prioritization
ITEM_TAGS = {
    # Wood items
    "oak_log": {"wood", "log", "tree", "oak"},
    "birch_log": {"wood", "log", "tree", "birch"},
    "spruce_log": {"wood", "log", "tree", "spruce"},
    "jungle_log": {"wood", "log", "tree", "jungle"},
    "acacia_log": {"wood", "log", "tree", "acacia"},
    "dark_oak_log": {"wood", "log", "tree", "dark_oak"},
    "oak_planks": {"wood", "planks", "building", "oak"},
    "birch_planks": {"wood", "planks", "building", "birch"},
    "spruce_planks": {"wood", "planks", "building", "spruce"},
    "jungle_planks": {"wood", "planks", "building", "jungle"},
    "acacia_planks": {"wood", "planks", "building", "acacia"},
    "dark_oak_planks": {"wood", "planks", "building", "dark_oak"},
    
    # Stone items
    "stone": {"stone", "building", "block"},
    "cobblestone": {"stone", "building", "block", "cobble"},
    "granite": {"stone", "building", "block", "granite"},
    "diorite": {"stone", "building", "block", "diorite"},
    "andesite": {"stone", "building", "block", "andesite"},
    
    # Tools
    "wooden_pickaxe": {"tool", "pickaxe", "wood", "mining"},
    "stone_pickaxe": {"tool", "pickaxe", "stone", "mining"},
    "iron_pickaxe": {"tool", "pickaxe", "iron", "mining"},
    "golden_pickaxe": {"tool", "pickaxe", "gold", "mining"},
    "diamond_pickaxe": {"tool", "pickaxe", "diamond", "mining"},
    "netherite_pickaxe": {"tool", "pickaxe", "netherite", "mining"},
    
    "wooden_axe": {"tool", "axe", "wood", "chopping"},
    "stone_axe": {"tool", "axe", "stone", "chopping"},
    "iron_axe": {"tool", "axe", "iron", "chopping"},
    "golden_axe": {"tool", "axe", "gold", "chopping"},
    "diamond_axe": {"tool", "axe", "diamond", "chopping"},
    "netherite_axe": {"tool", "axe", "netherite", "chopping"},
    
    "wooden_shovel": {"tool", "shovel", "wood", "digging"},
    "stone_shovel": {"tool", "shovel", "stone", "digging"},
    "iron_shovel": {"tool", "shovel", "iron", "digging"},
    "golden_shovel": {"tool", "shovel", "gold", "digging"},
    "diamond_shovel": {"tool", "shovel", "diamond", "digging"},
    "netherite_shovel": {"tool", "shovel", "netherite", "digging"},
    
    "wooden_hoe": {"tool", "hoe", "wood", "farming"},
    "stone_hoe": {"tool", "hoe", "stone", "farming"},
    "iron_hoe": {"tool", "hoe", "iron", "farming"},
    "golden_hoe": {"tool", "hoe", "gold", "farming"},
    "diamond_hoe": {"tool", "hoe", "diamond", "farming"},
    "netherite_hoe": {"tool", "hoe", "netherite", "farming"},
    
    # Weapons
    "wooden_sword": {"weapon", "sword", "wood", "combat"},
    "stone_sword": {"weapon", "sword", "stone", "combat"},
    "iron_sword": {"weapon", "sword", "iron", "combat"},
    "golden_sword": {"weapon", "sword", "gold", "combat"},
    "diamond_sword": {"weapon", "sword", "diamond", "combat"},
    "netherite_sword": {"weapon", "sword", "netherite", "combat"},
    
    # Armor
    "leather_helmet": {"armor", "helmet", "leather", "head"},
    "leather_chestplate": {"armor", "chestplate", "leather", "chest"},
    "leather_leggings": {"armor", "leggings", "leather", "legs"},
    "leather_boots": {"armor", "boots", "leather", "feet"},
    
    "iron_helmet": {"armor", "helmet", "iron", "head"},
    "iron_chestplate": {"armor", "chestplate", "iron", "chest"},
    "iron_leggings": {"armor", "leggings", "iron", "legs"},
    "iron_boots": {"armor", "boots", "iron", "feet"},
    
    "golden_helmet": {"armor", "helmet", "gold", "head"},
    "golden_chestplate": {"armor", "chestplate", "gold", "chest"},
    "golden_leggings": {"armor", "leggings", "gold", "legs"},
    "golden_boots": {"armor", "boots", "gold", "feet"},
    
    "diamond_helmet": {"armor", "helmet", "diamond", "head"},
    "diamond_chestplate": {"armor", "chestplate", "diamond", "chest"},
    "diamond_leggings": {"armor", "leggings", "diamond", "legs"},
    "diamond_boots": {"armor", "boots", "diamond", "feet"},
    
    "netherite_helmet": {"armor", "helmet", "netherite", "head"},
    "netherite_chestplate": {"armor", "chestplate", "netherite", "chest"},
    "netherite_leggings": {"armor", "leggings", "netherite", "legs"},
    "netherite_boots": {"armor", "boots", "netherite", "feet"},
    
    # Food
    "apple": {"food", "fruit", "apple"},
    "bread": {"food", "bread", "baked"},
    "cooked_beef": {"food", "meat", "cooked", "beef"},
    "cooked_chicken": {"food", "meat", "cooked", "chicken"},
    "cooked_porkchop": {"food", "meat", "cooked", "pork"},
    "cooked_mutton": {"food", "meat", "cooked", "mutton"},
    "cooked_rabbit": {"food", "meat", "cooked", "rabbit"},
    
    # Ores and Minerals
    "coal": {"ore", "mineral", "coal", "fuel"},
    "iron_ingot": {"ore", "mineral", "iron", "ingot"},
    "gold_ingot": {"ore", "mineral", "gold", "ingot"},
    "diamond": {"ore", "mineral", "diamond", "gem"},
    "emerald": {"ore", "mineral", "emerald", "gem"},
    "lapis_lazuli": {"ore", "mineral", "lapis", "gem"},
    "redstone": {"ore", "mineral", "redstone", "red"},
    "netherite_ingot": {"ore", "mineral", "netherite", "ingot"},
    
    # Redstone Components
    "redstone_torch": {"redstone", "component", "torch", "power"},
    "redstone_block": {"redstone", "component", "block", "power"},
    "repeater": {"redstone", "component", "repeater", "power"},
    "comparator": {"redstone", "component", "comparator", "power"},
    "piston": {"redstone", "component", "piston", "mechanism"},
    "sticky_piston": {"redstone", "component", "piston", "sticky", "mechanism"},
    "observer": {"redstone", "component", "observer", "mechanism"},
    "hopper": {"redstone", "component", "hopper", "storage"},
    
    # Decoration
    "painting": {"decoration", "art", "painting"},
    "item_frame": {"decoration", "frame", "display"},
    "flower_pot": {"decoration", "pot", "plant"},
    "torch": {"decoration", "light", "torch"},
    "lantern": {"decoration", "light", "lantern"},
    "soul_lantern": {"decoration", "light", "lantern", "soul"},
    
    # Storage
    "chest": {"storage", "container", "chest"},
    "barrel": {"storage", "container", "barrel"},
    "furnace": {"storage", "container", "furnace", "smelt"},
    "blast_furnace": {"storage", "container", "furnace", "smelt", "blast"},
    "smoker": {"storage", "container", "furnace", "smelt", "smoke"},
    "hopper": {"storage", "container", "hopper", "redstone"},
    
    # Transportation
    "minecart": {"transport", "minecart", "rail"},
    "chest_minecart": {"transport", "minecart", "rail", "storage"},
    "furnace_minecart": {"transport", "minecart", "rail", "power"},
    "boat": {"transport", "boat", "water"},
    "saddle": {"transport", "saddle", "horse"},
    
    # Special Items
    "ender_pearl": {"special", "teleport", "ender"},
    "ender_eye": {"special", "locate", "ender"},
    "nether_star": {"special", "beacon", "nether"},
    "dragon_egg": {"special", "dragon", "trophy"},
    "elytra": {"special", "flight", "wings"},
    "totem_of_undying": {"special", "totem", "undying"},
    
    # Brewing
    "brewing_stand": {"brewing", "stand", "potion"},
    "cauldron": {"brewing", "cauldron", "potion"},
    "blaze_powder": {"brewing", "blaze", "powder"},
    "ghast_tear": {"brewing", "ghast", "tear"},
    "magma_cream": {"brewing", "magma", "cream"},
    "fermented_spider_eye": {"brewing", "spider", "eye", "fermented"},
    
    # Enchanting
    "enchanting_table": {"enchanting", "table", "book"},
    "bookshelf": {"enchanting", "bookshelf", "book"},
    "book": {"enchanting", "book", "write"},
    "enchanted_book": {"enchanting", "book", "enchanted"},
    
    # Farming
    "wheat_seeds": {"farming", "seed", "wheat", "plant"},
    "carrot": {"farming", "vegetable", "carrot", "plant"},
    "potato": {"farming", "vegetable", "potato", "plant"},
    "beetroot_seeds": {"farming", "seed", "beetroot", "plant"},
    "pumpkin_seeds": {"farming", "seed", "pumpkin", "plant"},
    "melon_seeds": {"farming", "seed", "melon", "plant"},
    
    # Combat
    "bow": {"combat", "bow", "ranged"},
    "arrow": {"combat", "arrow", "ranged"},
    "shield": {"combat", "shield", "defense"},
    "crossbow": {"combat", "crossbow", "ranged"},
    "trident": {"combat", "trident", "ranged", "water"},
    
    # Utility
    "bucket": {"utility", "bucket", "liquid"},
    "water_bucket": {"utility", "bucket", "water"},
    "lava_bucket": {"utility", "bucket", "lava"},
    "flint_and_steel": {"utility", "flint", "steel", "fire"},
    "compass": {"utility", "compass", "navigation"},
    "clock": {"utility", "clock", "time"},
    "fishing_rod": {"utility", "fishing", "rod"},
    "shears": {"utility", "shears", "cut"},
    "lead": {"utility", "lead", "animal"},
    "name_tag": {"utility", "name", "tag", "animal"}
}

# Item version information
ITEM_VERSIONS = {
    # Beta 1.9 Prerelease items
    "blaze_rod": "Beta 1.9 Prerelease",
    "ghast_tear": "Beta 1.9 Prerelease",
    "gold_nugget": "Beta 1.9 Prerelease",
    "nether_wart": "Beta 1.9 Prerelease",
    
    # Beta 1.9 Prerelease 2 items
    "blaze_powder": "Beta 1.9 Prerelease 2",
    "fermented_spider_eye": "Beta 1.9 Prerelease 2",
    "glass_bottle": "Beta 1.9 Prerelease 2",
    "magma_cream": "Beta 1.9 Prerelease 2",
    "spider_eye": "Beta 1.9 Prerelease 2",
    "music_disc_13": "Beta 1.9 Prerelease 2",
    "music_disc_cat": "Beta 1.9 Prerelease 2",
    "music_disc_blocks": "Beta 1.9 Prerelease 2",
    "music_disc_chirp": "Beta 1.9 Prerelease 2",
    "music_disc_far": "Beta 1.9 Prerelease 2",
    "music_disc_mall": "Beta 1.9 Prerelease 2",
    "music_disc_mellohi": "Beta 1.9 Prerelease 2",
    "music_disc_stal": "Beta 1.9 Prerelease 2",
    "music_disc_strad": "Beta 1.9 Prerelease 2",
    "music_disc_ward": "Beta 1.9 Prerelease 2",
    "music_disc_11": "Beta 1.9 Prerelease 2",
    
    # Beta 1.9 Prerelease 3 items
    "ender_eye": "Beta 1.9 Prerelease 3",
    
    # Beta 1.9 Prerelease 4 items
    "glistering_melon_slice": "Beta 1.9 Prerelease 4",
    "potion": "Beta 1.9 Prerelease 4",
    "splash_potion": "Beta 1.9 Prerelease 4",
    
    # 1.1 items
    "spawn_egg": "1.1",
    
    # 1.2.1 items
    "bottle_o_enchanting": "1.2.1",
    "fire_charge": "1.2.1",
    
    # 1.3.1 items
    "book_and_quill": "1.3.1",
    "written_book": "1.3.1",
    "emerald": "1.3.1",
    "enchanted_golden_apple": "1.3.1",
    
    # 1.4.2 items
    "carrot": "1.4.2",
    "golden_carrot": "1.4.2",
    "potato": "1.4.2",
    "baked_potato": "1.4.2",
    "poisonous_potato": "1.4.2",
    "item_frame": "1.4.2",
    "carrot_on_a_stick": "1.4.2",
    "nether_star": "1.4.2",
    "pumpkin_pie": "1.4.2",
    "music_disc_wait": "1.4.3",
    
    # 1.4.6 items
    "enchanted_book": "1.4.6",
    "firework_rocket": "1.4.6",
    "firework_star": "1.4.6",
    
    # 1.5 items
    "nether_brick": "1.5",
    "nether_quartz": "1.5",
    
    # 1.6.1 items
    "diamond_horse_armor": "1.6.1",
    "golden_horse_armor": "1.6.1",
    "iron_horse_armor": "1.6.1",
    "lead": "1.6.1",
    "name_tag": "1.6.1",
    
    # 1.7.2 items
    "tropical_fish": "1.7.2",
    "cooked_salmon": "1.7.2",
    "pufferfish": "1.7.2",
    
    # 1.8 items
    "prismarine_crystals": "1.8",
    "prismarine_shard": "1.8",
    "cooked_mutton": "1.8",
    "cooked_rabbit": "1.8",
    "rabbit_foot": "1.8",
    "rabbit_hide": "1.8",
    "rabbit_stew": "1.8",
    
    # 1.9 items
    "spectral_arrow": "1.9",
    "tipped_arrow": "1.9",
    "beetroot": "1.9",
    "beetroot_seeds": "1.9",
    "beetroot_soup": "1.9",
    "chorus_fruit": "1.9",
    "popped_chorus_fruit": "1.9",
    "dragon_breath": "1.9",
    "lingering_potion": "1.9",
    "shield": "1.9",
    "elytra": "1.9",
    "end_crystal": "1.9",
    
    # 1.11 items
    "shulker_shell": "1.11",
    "totem_of_undying": "1.11",
    "iron_nugget": "1.11.1",
    
    # 1.12 items
    "knowledge_book": "1.12",
    
    # 1.13 items
    "trident": "1.13",
    "kelp": "1.13",
    "dried_kelp": "1.13",
    "scute": "1.13",
    "turtle_helmet": "1.13",
    "phantom_membrane": "1.13",
    "heart_of_the_sea": "1.13",
    "nautilus_shell": "1.13",
    
    # 1.14 items
    "crossbow": "1.14",
    "sweet_berries": "1.14",
    "suspicious_stew": "1.14",
    "leather_horse_armor": "1.14",
    
    # 1.15 items
    "honey_bottle": "1.15",
    "honeycomb": "1.15",
    
    # 1.16 items
    "netherite_ingot": "1.16",
    "netherite_scrap": "1.16",
    "netherite_sword": "1.16",
    "netherite_pickaxe": "1.16",
    "netherite_axe": "1.16",
    "netherite_shovel": "1.16",
    "netherite_hoe": "1.16",
    "netherite_helmet": "1.16",
    "netherite_chestplate": "1.16",
    "netherite_leggings": "1.16",
    "netherite_boots": "1.16",
    "warped_fungus_on_a_stick": "1.16",
    "music_disc_pigstep": "1.16",
    
    # 1.17 items
    "amethyst_shard": "1.17",
    "bundle": "1.17",
    "copper_ingot": "1.17",
    "spyglass": "1.17",
    "powder_snow_bucket": "1.17",
    "glow_item_frame": "1.17",
    "glow_ink_sac": "1.17",
    "glow_berries": "1.17",
    "raw_copper": "1.17",
    "raw_iron": "1.17",
    "raw_gold": "1.17",
    
    # 1.18 items
    "music_disc_otherside": "1.18",
    
    # 1.19 items
    "echo_shard": "1.19",
    "recovery_compass": "1.19",
    "music_disc_5": "1.19",
    "goat_horn": "1.19",
    
    # 1.20 items
    "bamboo_raft": "1.20",
    "cherry_boat": "1.20",
    "brush": "1.20",
    "torchflower_seeds": "1.20",
    "pitcher_pod": "1.20",
    "music_disc_relic": "1.20",
    
    # Smithing templates (1.20)
    "netherite_upgrade_smithing_template": "1.20",
    "sentry_armor_trim_smithing_template": "1.20",
    "dune_armor_trim_smithing_template": "1.20",
    "coast_armor_trim_smithing_template": "1.20",
    "wild_armor_trim_smithing_template": "1.20",
    "ward_armor_trim_smithing_template": "1.20",
    "eye_armor_trim_smithing_template": "1.20",
    "vex_armor_trim_smithing_template": "1.20",
    "tide_armor_trim_smithing_template": "1.20",
    "snout_armor_trim_smithing_template": "1.20",
    "rib_armor_trim_smithing_template": "1.20",
    "spire_armor_trim_smithing_template": "1.20",
    "wayfinder_armor_trim_smithing_template": "1.20",
    "shaper_armor_trim_smithing_template": "1.20",
    "silence_armor_trim_smithing_template": "1.20",
    "raiser_armor_trim_smithing_template": "1.20",
    "host_armor_trim_smithing_template": "1.20",
    
    # 1.20.5 items
    "armadillo_scute": "1.20.5",
    "wolf_armor": "1.20.5",
    "wind_charge": "1.20.5",
    "mace": "1.20.5",
    "breeze_rod": "1.20.5",
    "ominous_bottle": "1.20.5",
    "ominous_trial_key": "1.20.5",
    "trial_key": "1.20.5",
    "resin_brick": "1.20.5",
    
    # 1.21 items
    "music_disc_creator": "1.21",
    "music_disc_creator_music_box": "1.21",
    "music_disc_precipice": "1.21",
    "blue_egg": "1.21.5",
    "brown_egg": "1.21.5"
}

# Block version information
BLOCK_VERSIONS = {
    # Cave game tech test blocks
    "air": "pre-Classic",
    "stone": "pre-Classic",
    "grass_block": "pre-Classic",
    
    # Pre-Classic blocks
    "dirt": "pre-Classic rd-20090515",
    "cobblestone": "pre-Classic rd-20090515",
    "oak_planks": "pre-Classic rd-20090515",
    "oak_sapling": "pre-Classic rd-161348",
    
    # Classic 0.0.12a blocks
    "bedrock": "Classic 0.0.12a",
    "water": "Classic 0.0.12a",
    "lava": "Classic 0.0.12a",
    
    # Classic 0.0.14a blocks
    "sand": "Classic 0.0.14a",
    "gravel": "Classic 0.0.14a",
    "gold_ore": "Classic 0.0.14a",
    "iron_ore": "Classic 0.0.14a",
    "coal_ore": "Classic 0.0.14a",
    "oak_log": "Classic 0.0.14a",
    "oak_leaves": "Classic 0.0.14a",
    
    # Classic 0.0.19a blocks
    "sponge": "Classic 0.0.19a",
    "glass": "Classic 0.0.19a",
    
    # Classic 0.0.20a blocks
    "white_wool": "Classic 0.0.20a",
    "dandelion": "Classic 0.0.20a",
    "poppy": "Classic 0.0.20a",
    "brown_mushroom": "Classic 0.0.20a",
    "red_mushroom": "Classic 0.0.20a",
    "gold_block": "Classic 0.0.20a",
    "iron_block": "Classic 0.0.20a",
    
    # Classic 0.26 SURVIVAL TEST blocks
    "smooth_stone_slab": "Classic 0.26 SURVIVAL TEST",
    "bricks": "Classic 0.26 SURVIVAL TEST",
    "tnt": "Classic 0.26 SURVIVAL TEST",
    "bookshelf": "Classic 0.26 SURVIVAL TEST",
    "mossy_cobblestone": "Classic 0.26 SURVIVAL TEST",
    "obsidian": "Classic 0.26 SURVIVAL TEST",
    
    # Indev blocks
    "torch": "Indev 0.31 20091223-1457",
    "fire": "Indev 0.31 20100109-1939",
    "chest": "Indev 0.31 20100124-2119",
    "diamond_ore": "Indev 0.31 20100128-2200",
    "diamond_block": "Indev 0.31 20100128-2200",
    "crafting_table": "Indev 0.31 20100130",
    "wheat": "Indev 20100206-2034",
    "farmland": "Indev 20100206-2034",
    "furnace": "Indev 20100219",
    
    # Infdev blocks
    "oak_sign": "Infdev 20100607",
    "oak_door": "Infdev 20100607",
    "ladder": "Infdev 20100607",
    "rail": "Infdev 20100618",
    "spawner": "Infdev 20100625-2",
    "oak_stairs": "Infdev 20100629",
    "cobblestone_stairs": "Infdev 20100629",
    
    # Alpha v1.0.1 blocks
    "redstone_wire": "Alpha v1.0.1",
    "lever": "Alpha v1.0.1",
    "stone_pressure_plate": "Alpha v1.0.1",
    "iron_door": "Alpha v1.0.1",
    "oak_pressure_plate": "Alpha v1.0.1",
    "redstone_ore": "Alpha v1.0.1",
    "redstone_torch": "Alpha v1.0.1",
    "stone_button": "Alpha v1.0.1",
    
    # Alpha v1.0.4 blocks
    "snow": "Alpha v1.0.4",
    "ice": "Alpha v1.0.4",
    
    # Alpha v1.0.5 blocks
    "snow_block": "Alpha v1.0.5",
    
    # Alpha v1.0.6 blocks
    "cactus": "Alpha v1.0.6",
    
    # Alpha v1.0.11 blocks
    "clay": "Alpha v1.0.11",
    "sugar_cane": "Alpha v1.0.11",
    
    # Alpha v1.0.14 blocks
    "jukebox": "Alpha v1.0.14",
    
    # Alpha v1.0.17 blocks
    "oak_fence": "Alpha v1.0.17",
    
    # Alpha v1.2.0 blocks
    "carved_pumpkin": "Alpha v1.2.0",
    "netherrack": "Alpha v1.2.0",
    "soul_sand": "Alpha v1.2.0",
    "glowstone": "Alpha v1.2.0",
    "nether_portal": "Alpha v1.2.0",
    "jack_o_lantern": "Alpha v1.2.0",
    
    # Beta 1.2 blocks
    "spruce_log": "Beta 1.2",
    "birch_log": "Beta 1.2",
    "spruce_leaves": "Beta 1.2",
    "birch_leaves": "Beta 1.2",
    "lapis_ore": "Beta 1.2",
    "lapis_block": "Beta 1.2",
    "dispenser": "Beta 1.2",
    "sandstone": "Beta 1.2",
    "note_block": "Beta 1.2",
    "cake": "Beta 1.2",
    
    # Beta 1.3 blocks
    "red_bed": "Beta 1.3",
    "smooth_stone": "Beta 1.3",
    "sandstone_slab": "Beta 1.3",
    "petrified_oak_slab": "Beta 1.3",
    "cobblestone_slab": "Beta 1.3",
    "repeater": "Beta 1.3",
    
    # Beta 1.5 blocks
    "spruce_sapling": "Beta 1.5",
    "birch_sapling": "Beta 1.5",
    "powered_rail": "Beta 1.5",
    "detector_rail": "Beta 1.5",
    "cobweb": "Beta 1.5",
    "tallgrass": "Beta 1.6",
    "short_grass": "Beta 1.6",
    "fern": "Beta 1.6",
    "dead_bush": "Beta 1.6",
    "oak_trapdoor": "Beta 1.6",
    
    # Beta 1.7 blocks
    "sticky_piston": "Beta 1.7",
    "piston": "Beta 1.7",
    
    # Beta 1.8 Pre-release blocks
    "brick_slab": "Beta 1.8 Pre-release",
    "stone_brick_slab": "Beta 1.8 Pre-release",
    "infested_stone": "Beta 1.8 Pre-release",
    "infested_cobblestone": "Beta 1.8 Pre-release",
    "infested_stone_bricks": "Beta 1.8 Pre-release",
    "stone_bricks": "Beta 1.8 Pre-release",
    "brown_mushroom_block": "Beta 1.8 Pre-release",
    "mushroom_stem": "Beta 1.8 Pre-release",
    "red_mushroom_block": "Beta 1.8 Pre-release",
    "iron_bars": "Beta 1.8 Pre-release",
    "glass_pane": "Beta 1.8 Pre-release",
    "melon": "Beta 1.8 Pre-release",
    "pumpkin_stem": "Beta 1.8 Pre-release",
    "melon_stem": "Beta 1.8 Pre-release",
    "vines": "Beta 1.8 Pre-release",
    "oak_fence_gate": "Beta 1.8 Pre-release",
    "brick_stairs": "Beta 1.8 Pre-release",
    "stone_brick_stairs": "Beta 1.8 Pre-release",
    
    # Beta 1.9 Prerelease blocks
    "nether_brick_slab": "Beta 1.9 Prerelease",
    "mycelium": "Beta 1.9 Prerelease",
    "lily_pad": "Beta 1.9 Prerelease",
    "nether_bricks": "Beta 1.9 Prerelease",
    "nether_brick_fence": "Beta 1.9 Prerelease",
    "nether_brick_stairs": "Beta 1.9 Prerelease",
    "nether_wart": "Beta 1.9 Prerelease",
    
    # Beta 1.9 Prerelease 3 blocks
    "enchanting_table": "Beta 1.9 Prerelease 3",
    "brewing_stand": "Beta 1.9 Prerelease 3",
    "cauldron": "Beta 1.9 Prerelease 3",
    "end_portal": "Beta 1.9 Prerelease 3",
    "end_portal_frame": "Beta 1.9 Prerelease 3",
    
    # Beta 1.9 Prerelease 4 blocks
    "end_stone": "Beta 1.9 Prerelease 4",
    
    # Beta 1.9 Prerelease 6 blocks
    "dragon_egg": "Beta 1.9 Prerelease 6",
    
    # 12w03a blocks
    "jungle_log": "12w03a",
    "jungle_leaves": "12w03a",
    "jungle_sapling": "12w03a",
    
    # 12w07a blocks
    "redstone_lamp": "12w07a",
    
    # 1.2 blocks
    "chiseled_stone_bricks": "1.2",
    
    # 1.2.4 blocks
    "spruce_planks": "1.2.4",
    "birch_planks": "1.2.4",
    "jungle_planks": "1.2.4",
    "chiseled_sandstone": "1.2.4",
    "cut_sandstone": "1.2.4",
    
    # 12w17a blocks
    "oak_slab": "12w17a",
    "spruce_slab": "12w17a",
    "birch_slab": "12w17a",
    "jungle_slab": "12w17a",
    
    # 12w19a blocks
    "cocoa": "12w19a",
    
    # 12w21a blocks
    "sandstone_stairs": "12w21a",
    "emerald_ore": "12w21a",
    "ender_chest": "12w21a",
    
    # 12w22a blocks
    "tripwire_hook": "12w22a",
    "tripwire": "12w22a",
    "emerald_block": "12w22a",
    
    # 12w25a blocks
    "spruce_stairs": "12w25a",
    "birch_stairs": "12w25a",
    "jungle_stairs": "12w25a",
    
    # 12w30d blocks
    "oak_wood": "12w30d",
    "spruce_wood": "12w30d",
    "birch_wood": "12w30d",
    "jungle_wood": "12w30d",
    "acacia_wood": "12w30d",
    "acacia_log": "12w30d",
    "acacia_sapling": "12w30d",
    "acacia_leaves": "12w30d",
    "dark_oak_wood": "12w30d",
    "dark_oak_log": "12w30d",
    "dark_oak_sapling": "12w30d",
    "dark_oak_leaves": "12w30d",
    
    # 12w32a blocks
    "beacon": "12w32a",
    "command_block": "12w32a",
    "cobblestone_wall": "12w32a",
    
    # 12w34a blocks
    "flower_pot": "12w34a",
    "mossy_cobblestone_wall": "12w34a",
    "wooden_button": "12w34a",
    
    # 12w36a blocks
    "skeleton_skull": "12w36a",
    "wither_skeleton_skull": "12w36a",
    "zombie_head": "12w36a",
    "creeper_head": "12w36a",
    "player_head": "12w36a",
    
    # 12w41a blocks
    "anvil": "12w41a",
    
    # 13w01a blocks
    "block_of_redstone": "13w01a",
    "daylight_sensor": "13w01a",
    "hopper": "13w01a",
    "nether_quartz_ore": "13w01a",
    "redstone_comparator": "13w01a",
    "trapped_chest": "13w01a",
    "light_weighted_pressure_plate": "13w01a",
    "heavy_weighted_pressure_plate": "13w01a",
    
    # 13w02a blocks
    "activator_rail": "13w02a",
    "block_of_quartz": "13w02a",
    "chiseled_quartz_block": "13w02a",
    "pillar_quartz_block": "13w02a",
    "quartz_stairs": "13w02a",
    "quartz_slab": "13w02a",
    
    # 13w03a blocks
    "dropper": "13w03a",
    
    # 13w16a blocks
    "white_carpet": "13w16a",
    "light_gray_carpet": "13w16a",
    "gray_carpet": "13w16a",
    "black_carpet": "13w16a",
    "brown_carpet": "13w16a",
    "red_carpet": "13w16a",
    "orange_carpet": "13w16a",
    "yellow_carpet": "13w16a",
    "lime_carpet": "13w16a",
    "green_carpet": "13w16a",
    "cyan_carpet": "13w16a",
    "light_blue_carpet": "13w16a",
    "blue_carpet": "13w16a",
    "purple_carpet": "13w16a",
    "magenta_carpet": "13w16a",
    "pink_carpet": "13w16a",
    "hay_block": "13w16a",
    
    # 13w17a blocks
    "terracotta": "13w17a",
    
    # 13w18a blocks
    "coal_block": "13w18a",
    
    # 13w36a blocks
    "large_fern": "13w36a",
    "allium": "13w36a",
    "azure_bluet": "13w36a",
    "blue_orchid": "13w36a",
    "lilac": "13w36a",
    "oxeye_daisy": "13w36a",
    "peony": "13w36a",
    "rose_bush": "13w36a",
    "sunflower": "13w36a",
    "red_tulip": "13w36a",
    "orange_tulip": "13w36a",
    "white_tulip": "13w36a",
    "pink_tulip": "13w36a",
    "tall_grass": "13w36a",
    "coarse_dirt": "13w36a",
    "infested_mossy_stone_bricks": "13w36a",
    "infested_cracked_stone_bricks": "13w36a",
    "infested_chiseled_stone_bricks": "13w36a",
    "packed_ice": "13w36a",
    "podzol": "13w36a",
    
    # 13w39a blocks
    "red_sand": "13w39a",
    
    # 13w41a blocks
    "white_stained_glass": "13w41a",
    "light_gray_stained_glass": "13w41a",
    "gray_stained_glass": "13w41a",
    "black_stained_glass": "13w41a",
    "brown_stained_glass": "13w41a",
    "red_stained_glass": "13w41a",
    "orange_stained_glass": "13w41a",
    "yellow_stained_glass": "13w41a",
    "lime_stained_glass": "13w41a",
    "green_stained_glass": "13w41a",
    "cyan_stained_glass": "13w41a",
    "light_blue_stained_glass": "13w41a",
    "blue_stained_glass": "13w41a",
    "purple_stained_glass": "13w41a",
    "magenta_stained_glass": "13w41a",
    "pink_stained_glass": "13w41a",
    "white_stained_glass_pane": "13w41a",
    "light_gray_stained_glass_pane": "13w41a",
    "gray_stained_glass_pane": "13w41a",
    "black_stained_glass_pane": "13w41a",
    "brown_stained_glass_pane": "13w41a",
    "red_stained_glass_pane": "13w41a",
    "orange_stained_glass_pane": "13w41a",
    "yellow_stained_glass_pane": "13w41a",
    "lime_stained_glass_pane": "13w41a",
    "green_stained_glass_pane": "13w41a",
    "cyan_stained_glass_pane": "13w41a",
    "light_blue_stained_glass_pane": "13w41a",
    "blue_stained_glass_pane": "13w41a",
    "purple_stained_glass_pane": "13w41a",
    "magenta_stained_glass_pane": "13w41a",
    "pink_stained_glass_pane": "13w41a",
    
    # 14w02a blocks
    "granite": "14w02a",
    "polished_granite": "14w02a",
    "diorite": "14w02a",
    "polished_diorite": "14w02a",
    "andesite": "14w02a",
    "polished_andesite": "14w02a",
    "slime_block": "14w02a",
    
    # 14w05a blocks
    "barrier": "14w05a",
    
    # 14w07a blocks
    "iron_trapdoor": "14w07a",
    
    # 14w25a blocks
    "prismarine": "14w25a",
    "prismarine_bricks": "14w25a",
    "dark_prismarine": "14w25a",
    "sea_lantern": "14w25a",
    "wet_sponge": "14w25a",
    
    # 14w30a blocks
    "white_banner": "14w30a",
    "light_gray_banner": "14w30a",
    "gray_banner": "14w30a",
    "black_banner": "14w30a",
    "brown_banner": "14w30a",
    "red_banner": "14w30a",
    "orange_banner": "14w30a",
    "yellow_banner": "14w30a",
    "lime_banner": "14w30a",
    "green_banner": "14w30a",
    "cyan_banner": "14w30a",
    "light_blue_banner": "14w30a",
    "blue_banner": "14w30a",
    "purple_banner": "14w30a",
    "magenta_banner": "14w30a",
    "pink_banner": "14w30a",
    
    # 14w32a blocks
    "armor_stand": "14w32a",
    "red_sandstone": "14w32a",
    "cut_red_sandstone": "14w32a",
    "chiseled_red_sandstone": "14w32a",
    "smooth_red_sandstone": "14w32a",
    "red_sandstone_slab": "14w32a",
    "red_sandstone_stairs": "14w32a",
    
    # 14w32b blocks
    "spruce_fence": "14w32b",
    "birch_fence": "14w32b",
    "jungle_fence": "14w32b",
    "acacia_fence": "14w32b",
    "dark_oak_fence": "14w32b",
    "spruce_fence_gate": "14w32b",
    "birch_fence_gate": "14w32b",
    "jungle_fence_gate": "14w32b",
    "acacia_fence_gate": "14w32b",
    "dark_oak_fence_gate": "14w32b",
    
    # 14w32d blocks
    "spruce_door": "14w32d",
    "birch_door": "14w32d",
    "jungle_door": "14w32d",
    "acacia_door": "14w32d",
    "dark_oak_door": "14w32d",
    
    # 15w31a blocks
    "dirt_path": "15w31a",
    "structure_block": "15w31a",
    "dragon_head": "15w31a",
    "end_gateway": "15w31a",
    "end_rod": "15w31a",
    "end_stone_bricks": "15w31a",
    "purpur_block": "15w31a",
    "purpur_pillar": "15w31a",
    "purpur_slab": "15w31a",
    "purpur_stairs": "15w31a",
    "chorus_plant": "15w31a",
    "chorus_flower": "15w31a",
    
    # 15w34a blocks
    "chain_command_block": "15w34a",
    "repeating_command_block": "15w34a",
    
    # 15w42a blocks
    "frosted_ice": "15w42a",
    
    # 16w20a blocks
    "bone_block": "16w20a",
    "magma_block": "16w20a",
    "nether_wart_block": "16w20a",
    "red_nether_bricks": "16w20a",
    "structure_void": "16w20a"
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
