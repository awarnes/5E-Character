"""
Serializers for database models.
"""

# DRF Imports:
from rest_framework import serializers

# Model Imports
from spells.models import Spell
from character.models import Character


class SpellModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spell

        fields = ('name', 'school', 'level', 'available_to', 'cast_time', 'distance', 'duration', 'concentration',
                  'ritual', 'material', 'somatic', 'verbal', 'specific_materials', 'description', 'save_type',
                  'damage_dice_number', 'damage_dice_size', 'damage_dice_bonus', 'damage_type', 'targets',
                  'higher_level', 'special', 'phb_page', 'raw_materials')

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
                  'armor_inv', 'weapons_inv', 'get_char_level')

                  # 'get_ability_bonus', 'get_passive_score',
                  # 'get_prof_bonus', 'get_initiative_bonus', 'get_armor_class',)