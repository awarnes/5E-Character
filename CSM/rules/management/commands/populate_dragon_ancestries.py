# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import DragonAncestry, DamageType


class Command(BaseCommand):
    """Command to populate the database with all Dragon Ancestries for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Dragon Ancestries from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Dragon Ancestries-Table 1.csv') as f:
            ancestries = pd.read_csv(f, delimiter=',')

        ancestries = ancestries.dropna()

        for ancestry in ancestries.iterrows():

            ancestry_entry = DragonAncestry.objects.create(
                name=ancestry[1][0],
                description=ancestry[1][1],
                breath_weapon_size=ancestry[1][3],
                breath_weapon_save=ancestry[1][4],
            )

            damage_type = ancestry[1][2]

            damage_type = DamageType.objects.get(name__iexact=damage_type)

            ancestry_entry.damage_type = damage_type

            ancestry_entry.save()
