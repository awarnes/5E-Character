from rest_framework import serializers

from spells.models import Spell


class SpellModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spell

        fields = ('name', 'school', 'level', 'available_to', 'cast_time', 'distance', 'duration', 'concentration',
                  'ritual', 'material', 'somatic', 'verbal', 'specific_materials', 'description', 'save_type',
                  'damage_dice_number', 'damage_dice_size', 'damage_dice_bonus', 'damage_type', 'targets',
                  'higher_level', 'special', 'phb_page', 'raw_materials')