# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from equipment.models import Weapon


class Command(BaseCommand):
    """Command to populate the database with all spells for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the normal Weapons from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/5E Rules CSVs/Weapons-Table 1.csv') as f:
            weapons = pd.read_csv(f, delimiter=',')

        weapons = weapons.dropna()

        for weapon in weapons.iterrows():

            weapon_entry = Weapon(
                name=weapon[1][0],
                item_type=weapon[1][1],
                description=weapon[1][2],
                weight=weapon[1][3],
                material=weapon[1][4],
                cost_copper=weapon[1][5],
                cost_silver=weapon[1][6],
                cost_gold=weapon[1][7],
                cost_platinum=weapon[1][8],
                special=weapon[1][9],

                weapon_type=weapon[1][10],
                melee_or_ranged=weapon[1][11],
                normal_range=weapon[1][12],
                max_range=weapon[1][13],
                damage_dice_num=weapon[1][14],
                damage_dice_size=weapon[1][15],
                damage_dice_bonus=weapon[1][16],
            )

            base_damage_type = weapon[1][16]

            weapon_entry.base_damage_type.add(base_damage_type)

            properties = weapon[1][17].split(', ')

            for property in properties:
                weapon_entry.properties.add(property)

            weapon_entry.save()