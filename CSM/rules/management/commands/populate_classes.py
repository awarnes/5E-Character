# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import Class


class Command(BaseCommand):
    """Command to populate the database with all skills for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Classes from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/5E Rules CSVs/Classes-Table 1.csv') as f:
            classes = pd.read_csv(f, delimiter=',')

        classes = classes.dropna()

        for klass in classes.iterrows():

            class_entry = Class(
                name=klass[1][0],
                description=klass[1][1],
                hit_die_size=klass[1][2],
                primary_ability_1=klass[1][3],
                primary_ability_2=klass[1][4],
                saving_throw_1=klass[1][5],
                saving_throw_2=klass[1][6],
                starting_gold=klass[1][7],
            )

            class_tool_starts = klass[1][11].split(', ')

            for tool in class_tool_starts:
                class_entry.starting_tools.add(tool)

            class_weapon_starts = klass[1][8].split(', ')

            for weapon in class_weapon_starts:
                class_entry.starting_weapons.add(weapon)

            class_armor_starts = klass[1][9].split(', ')

            for armor in class_armor_starts:
                class_entry.starting_armor.add(armor)

            class_item_starts = klass[1][10].split(', ')

            for item in class_item_starts:
                class_entry.starting_items.add(item)

            klass_features = klass[1][12].split(', ')

            for feature in klass_features:
                class_entry.features.add(feature)

            klass_prestige = klass[1][13].split(', ')

            for prestige in klass_prestige:
                class_entry.prestige_classes.add(prestige)

            class_entry.save()
