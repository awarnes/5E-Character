# python imports
import re

# django imports
from django.core.management.base import BaseCommand

# module level imports
from utils.spells import SPELLS
from spells.models import Spell

SPELL_SCHOOL = {
        'Abjuration': 'Abjuration',
        'Conjuration': 'Conjuration',
        'Divination': 'Divination',
        'Enchantment': 'Enchantment',
        'Evocation': 'Evocation',
        'Illusion': 'Illusion',
        'Necromancy': 'Necromancy',
        'Transmutation': 'Transmutation',
}

CAST_TIME = {
    '1 Action': '1 Action',
    '1 Bonus Action': '1 Bonus Action',
    '1 Reaction': '1 Reaction',
    '1 Minute': '1 Minute',
    '10 Minutes': '10 Minutes',
    '1 Hour': '1 Hour',
    '8 Hours': '8 Hours',
    '12 Hours': '12 Hours',
    '24 Hours': '24 Hours',
    '1 Action or 8 Hours': '1 Action or 8 Hours',
}

SPELL_LEVELS = {
    'Cantrip': 'Cantrip',
    '1': '1st-level',
    '2': '2nd-level',
    '3': '3rd-level',
    '4': '4th-level',
    '5': '5th-level',
    '6': '6th-level',
    '7': '7th-level',
    '8': '8th-level',
    '9': '9th-level',
}


class Command(BaseCommand):
    """Command to populate the database with all spells for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Spells from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        for spell in SPELLS:
            spell_entry = Spell(
                name=spell['name'],
                distance=spell['range'],
                ritual=spell['ritual'],
            )

            if len(spell['classes']) > 1:
                spell_entry.available_to = ''
                for i in range(len(spell['classes'])):
                    spell_entry.available_to += spell['classes'][i].title() + ', '
            else:
                spell_entry.available_to = spell['classes'][0].title()

            if 'components' in spell.keys():
                spell_entry.somatic = spell['components']['somatic']
                spell_entry.verbal = spell['components']['verbal']
                spell_entry.material = spell['components']['material']

                if spell_entry.material:
                    spell_entry.specific_materials = ''
                    for i in range(len(spell['components']['materials_needed'])):
                        spell_entry.specific_materials += spell['components']['materials_needed'][i] + ', '

            if 'description' in spell.keys():
                spell_entry.description = spell['description']

                dice_number = re.findall(r'\d+(?=d)', spell['description'])
                if len(dice_number) > 0:
                    spell_entry.damage_dice_number = dice_number[0]

                dice_size = re.findall(r'(?<=d)\d+', spell['description'])
                if len(dice_size) > 0:
                    spell_entry.damage_dice_size = dice_size[0]

                s_throw = re.findall(r"[A-Z]\w+(?= saving throw)", spell['description'])
                if len(s_throw) == 1:
                    s_throw = s_throw[0][:3].upper()
                    spell_entry.save_type = s_throw

            if spell['level'] == 'cantrip':
                spell_entry.level = 'Cantrip'
            else:
                spell_entry.level = SPELL_LEVELS[spell['level']]

            if 'higher_levels' in spell.keys():
                spell_entry.higher_level = spell['higher_levels']

            if 'school' in spell.keys():
                spell_entry.school = SPELL_SCHOOL[spell['school'].title()]

            if 'casting_time' in spell.keys():
                if 'reaction' in spell['casting_time']:
                    spell_entry.cast_time = CAST_TIME['1 Reaction']

                else:
                    spell_entry.cast_time = spell['casting_time'].title()

            if 'Concentration' in spell['duration']:
                spell_entry.concentration = True
                spell_entry.duration = spell['duration'][15:].title()
            else:
                spell_entry.concentration = False
                spell_entry.duration = spell['duration']

            spell_entry.save()
