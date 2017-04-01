"""
Serializers for database models.
"""

# DRF Imports:
from rest_framework import serializers

# Model Imports
from spells.models import Spell
from character.models import Character
from equipment.models import Weapon, WeaponProperty, Armor, Item, Tool, MountAndVehicle
from rules.models import (Subrace, Race, PrestigeClass, Class, Feature, Background,
                          Skill, Language, DamageType, Condition, Alignment)


class SpellModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spell

        fields = ('name', 'school', 'level', 'available_to', 'cast_time', 'distance', 'duration', 'concentration',
                  'ritual', 'material', 'somatic', 'verbal', 'specific_materials', 'description', 'save_type',
                  'damage_dice_number', 'damage_dice_size', 'damage_dice_bonus', 'damage_type', 'targets',
                  'higher_level', 'special', 'phb_page', 'raw_materials', 'slug', 'srd',)


class CharacterModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character

        fields = ('username', 'char_name', 'description', 'portrait', 'char_age', 'char_height', 'char_weight',
                  'char_skin_color', 'char_hair_color', 'char_eye_color', 'personality', 'ideals', 'bonds', 'flaws',
                  'allies', 'organizations', 'char_classes', 'char_race', 'char_background', 'alignment', 'char_xp',
                  'STR_score', 'DEX_score', 'CON_score', 'INT_score', 'WIS_score', 'CHA_score',
                  'STR_saving_throw', 'DEX_saving_throw', 'CON_saving_throw', 'INT_saving_throw', 'WIS_saving_throw',
                  'CHA_saving_throw', 'features', 'conditions', 'death_fails', 'death_successes', 'max_health',
                  'current_health', 'temp_addtl_hp', 'speed', 'inspiration', 'spell_book', 'tools_inv', 'items_inv',
                  'armor_inv', 'weapons_inv', 'get_char_level', 'slug', 'spell_slots_1_current', 'spell_slots_2_current',
                  'spell_slots_3_current', 'spell_slots_4_current', 'spell_slots_5_current', 'spell_slots_6_current',
                  'spell_slots_7_current', 'spell_slots_8_current', 'spell_slots_9_current', 'spell_slots_1_maximum',
                  'spell_slots_2_maximum', 'spell_slots_3_maximum', 'spell_slots_4_maximum', 'spell_slots_5_maximum',
                  'spell_slots_6_maximum', 'spell_slots_7_maximum', 'spell_slots_8_maximum', 'spell_slots_9_maximum',
                  'has_point_tracking', 'max_points', 'current_points'
                  # 'get_ability_bonus', 'get_passive_score',
                  # 'get_prof_bonus', 'get_initiative_bonus', 'get_armor_class',
                  )


# Equipment Serializers:
class DamageTypeModelSerializer(serializers.ModelSerializer):
    """Serializer for the DamageType model (Is a rule, but required by weapons)."""

    class Meta:
        model = DamageType

        fields = ('name', 'description', 'slug', 'srd',)


class WeaponPropertyModelSerializer(serializers.ModelSerializer):
    """Serializer for the WeaponProperty model."""

    class Meta:
        model = WeaponProperty

        fields = ('name', 'description', 'slug', 'srd',)


class ItemModelSerializer(serializers.ModelSerializer):
    """Serializer for the Item model."""

    class Meta:
        model = Item

        fields = ('name', 'item_type', 'description', 'weight', 'material', 'cost_copper', 'cost_silver', 'cost_gold',
                  'cost_platinum', 'special', 'uses', 'space', 'slug', 'srd',)


class ToolModelSerializer(serializers.ModelSerializer):
    """Serializer for the Tool model."""

    class Meta:
        model = Tool

        fields = ('name', 'item_type', 'description', 'weight', 'material', 'cost_copper', 'cost_silver', 'cost_gold',
                  'cost_platinum', 'special', 'requires_proficiency', 'tool_type', 'slug', 'srd',)


class WeaponModelSerializer(serializers.ModelSerializer):
    """Serializer for the Weapon model."""

    properties = WeaponPropertyModelSerializer(many=True)
    base_damage_type = DamageTypeModelSerializer(many=True)

    class Meta:
        model = Weapon

        fields = ('name', 'item_type', 'description', 'weight', 'material', 'cost_copper', 'cost_silver', 'cost_gold',
                  'cost_platinum', 'special', 'weapon_type', 'melee_or_ranged', 'normal_range', 'max_range',
                  'damage_dice_number', 'damage_dice_size', 'damage_dice_bonus', 'base_damage_type', 'properties', 'slug', 'srd',)


class ArmorModelSerializer(serializers.ModelSerializer):
    """Serializer for the Armor model."""

    class Meta:
        model = Armor

        fields = ('name', 'item_type', 'description', 'weight', 'material', 'cost_copper', 'cost_silver', 'cost_gold',
                  'cost_platinum', 'special', 'armor_type', 'base_armor_class', 'bonus_armor_class', 'dexterity_modifier',
                  'don_time', 'doff_time', 'req_str', 'stealth_disadvantage', 'slug', 'srd',)


class MountAndVehicleModelSerializer(serializers.ModelSerializer):
    """Serializer for the MountAndVehicle model."""

    class Meta:
        model = MountAndVehicle

        fields = ('name', 'item_type', 'description', 'weight', 'material', 'cost_copper', 'cost_silver', 'cost_gold',
                  'cost_platinum', 'special', 'speed', 'carrying_capacity', 'vehicle_type', 'slug', 'srd',)


# Rules Model Serializers:
class LanguageModelSerializer(serializers.ModelSerializer):
    """Serializer for the Language model."""

    class Meta:
        model = Language

        fields = ('name', 'description', 'typical_speakers', 'script', 'slug', 'srd',)


class ConditionModelSerializer(serializers.ModelSerializer):
    """Serializer for the Condition model."""

    class Meta:
        model = Condition

        fields = ('name', 'description', 'slug', 'srd',)


class AlignmentModelSerializer(serializers.ModelSerializer):
    """Serializer for the Alignment model."""

    class Meta:
        model = Alignment

        fields = ('name', 'description', 'slug', 'srd', 'examples',)


class SkillModelSerializer(serializers.ModelSerializer):
    """Serializer for the Skill model."""

    class Meta:
        model = Skill

        fields = ('name', 'description', 'associated_ability', 'example_tasks', 'slug', 'srd',)


class FeatureModelSerializer(serializers.ModelSerializer):
    """Serializer for the Feature model."""

    class Meta:
        model = Feature

        fields = ('name', 'description', 'slug', 'srd',)


class SubraceModelSerializer(serializers.ModelSerializer):
    """Serializer for the Subrace model."""

    features = FeatureModelSerializer(many=True)
    subrace_tool_starts = ToolModelSerializer(many=True)
    subrace_weapon_starts = WeaponModelSerializer(many=True)
    subrace_armor_starts = ArmorModelSerializer(many=True)
    subrace_item_starts = ItemModelSerializer(many=True)

    class Meta:
        model = Subrace

        fields = ('name', 'description', 'ability_score_1', 'ability_score_1_bonus', 'ability_score_2',
                  'ability_score_2_bonus', 'features', 'subrace_tool_starts', 'subrace_weapon_starts',
                  'subrace_armor_starts', 'subrace_item_starts', 'slug', 'srd',)


class RaceModelSerializer(serializers.ModelSerializer):
    """Serializer for the Race model."""

    features = FeatureModelSerializer(many=True)
    subraces = SubraceModelSerializer(many=True)
    race_tool_starts = ToolModelSerializer(many=True)
    race_weapon_starts = WeaponModelSerializer(many=True)
    race_armor_starts = ArmorModelSerializer(many=True)
    race_item_starts = ItemModelSerializer(many=True)

    class Meta:
        model = Race

        fields = ('name', 'description', 'ability_score_1', 'ability_score_1_bonus', 'ability_score_2',
                  'ability_score_2_bonus', 'features', 'age_adult', 'age_mortality', 'typical_alignment', 'size',
                  'typical_height_min', 'typical_height_max', 'typical_weight_min', 'typical_weight_max',
                  'speed', 'speed_special', 'features', 'race_tool_starts', 'race_weapon_starts', 'race_armor_starts',
                  'race_item_starts', 'subraces', 'slug', 'srd',)


class PrestigeClassModelSerializer(serializers.ModelSerializer):
    """Serializer for the PrestigeClass model."""

    features = FeatureModelSerializer(many=True)

    class Meta:
        model = PrestigeClass

        fields = ('name', 'description', 'features', 'slug', 'srd',)


class ClassModelSerializer(serializers.ModelSerializer):
    """Serializer for the Class model."""

    prestige_classes = PrestigeClassModelSerializer(many=True)
    features = FeatureModelSerializer(many=True)
    starting_weapons = WeaponModelSerializer(many=True)
    starting_armor = ArmorModelSerializer(many=True)
    starting_items = ItemModelSerializer(many=True)
    starting_tools = ToolModelSerializer(many=True)

    class Meta:
        model = Class

        fields = ('name', 'description', 'hit_die_size', 'primary_ability_1', 'primary_ability_2', 'saving_throw_1',
                  'saving_throw_2', 'starting_gold', 'starting_weapons', 'starting_armor', 'starting_items',
                  'starting_tools', 'features', 'prestige_classes', 'slug', 'srd',)


class BackgroundModelSerializer(serializers.ModelSerializer):
    """Serializer for the Background model."""

    features = FeatureModelSerializer(many=True)
    tool_starts = ToolModelSerializer(many=True)
    item_starts = ItemModelSerializer(many=True)
    weapon_starts = WeaponModelSerializer(many=True)
    armor_starts = ArmorModelSerializer(many=True)

    class Meta:
        model = Background

        fields = ('name', 'description', 'languages', 'features', 'gold_start', 'tool_starts', 'item_starts',
                  'weapon_starts', 'armor_starts', 'suggested_personality_traits', 'suggested_ideals',
                  'suggested_bonds', 'suggested_flaws', 'slug', 'srd',)
