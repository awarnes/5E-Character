# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from equipment.models import Item



class Command(BaseCommand):
    """Command to populate the database with all spells for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the base Items from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Items-Table 1.csv') as f:
            items = pd.read_csv(f, delimiter=',')

        items = items.dropna()

        for item in items.iterrows():

            item_entry = Item(
                name=item[1][0],
                item_type=item[1][1],
                description=item[1][2],
                weight=item[1][3],
                material=item[1][4],
                cost_copper=item[1][5],
                cost_silver=item[1][6],
                cost_gold=item[1][7],
                cost_platinum=item[1][8],
                special=item[1][9],

                uses=item[1][10],
                space=item[1][11],
            )

            item_entry.save()