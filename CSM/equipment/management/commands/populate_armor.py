# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from equipment.models import Armor


class Command(BaseCommand):
    """Command to populate the database with all spells for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the base Armor from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/5E Rules CSVs/Armor-Table 1.csv') as f:
            armors = pd.read_csv(f, delimiter=',')

        armors = armors.dropna()

        for armor in armors.iterrows():
            # import pdb;pdb.set_trace()
            Armor.objects.create(
                name=armor[1][0],
                item_type=armor[1][1],
                description=armor[1][2],
                weight=armor[1][3],
                material=armor[1][4],
                cost_copper=armor[1][5],
                cost_silver=armor[1][6],
                cost_gold=armor[1][7],
                cost_platinum=armor[1][8],
                special=armor[1][9],

                armor_type=armor[1][10],
                base_armor_class=armor[1][11],
                bonus_armor_class=armor[1][12],
                dexterity_modifier=armor[1][13],
                dexterity_modifier_max=armor[1][14],
                don_time=armor[1][15],
                doff_time=armor[1][16],
                req_str=armor[1][17],
                stealth_disadvantage=armor[1][18],
            )
