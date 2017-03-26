# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import DamageType


class Command(BaseCommand):
    """Command to populate the database with all spells for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Damage Types from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Damage Types-Table 1.csv') as f:
            damage_types = pd.read_csv(f, delimiter=',')

        # features = features.ix[:,'name':'description':'associated_ability':'example_tasks']

        damage_types = damage_types.dropna()

        for damage_type in damage_types.iterrows():

            damage_type_entry = DamageType(
                name=damage_type[1][0],
                description=damage_type[1][1],
            )

            damage_type_entry.save()