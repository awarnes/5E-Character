# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import LandType
from spells.models import Spell


class Command(BaseCommand):
    """Command to populate the database with all Land Types for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Land Types from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/5E Rules CSVs/Land Types-Table 1.csv') as f:
            types = pd.read_csv(f, delimiter=',')

        types = types.dropna()

        for type in types.iterrows():

            land_entry = LandType.objects.create(
                name=type[1][0],
                description=type[1][1],
            )

            circle_spells_3 = type[1][2].split(', ')

            for spell_name in circle_spells_3:
                spell = Spell.objects.filter(name__icontains=spell_name)

                land_entry.circle_spells_3.add(spell[0])

            circle_spells_5 = type[1][3].split(', ')

            for spell_name in circle_spells_5:
                spell = Spell.objects.filter(name__icontains=spell_name)

                land_entry.circle_spells_5.add(spell[0])

            circle_spells_7 = type[1][4].split(', ')

            for spell_name in circle_spells_7:
                spell = Spell.objects.filter(name__icontains=spell_name)

                land_entry.circle_spells_7.add(spell[0])

            circle_spells_9 = type[1][5].split(', ')

            for spell_name in circle_spells_9:
                spell = Spell.objects.filter(name__icontains=spell_name)

                land_entry.circle_spells_9.add(spell[0])
