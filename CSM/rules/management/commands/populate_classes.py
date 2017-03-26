# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import Class, PrestigeClass, Feature
from equipment.models import Weapon, Item, Tool, Armor


class Command(BaseCommand):
    """Command to populate the database with all skills for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Classes from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Classes-Table 1.csv') as f:
            classes = pd.read_csv(f, delimiter=',')

        classes = classes.dropna()

        for klass in classes.iterrows():

            class_entry = Class.objects.create(
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

            for tool_name in class_tool_starts:

                tool = Tool.objects.get(name=tool_name)

                class_entry.starting_tools.add(tool)

            class_weapon_starts = klass[1][8].split(', ')

            for weapon_name in class_weapon_starts:

                weapon = Weapon.objects.get(name=weapon_name)

                class_entry.starting_weapons.add(weapon)

            class_armor_starts = klass[1][9].split(', ')

            for armor_name in class_armor_starts:

                armor = Armor.objects.get(name=armor_name)

                class_entry.starting_armor.add(armor)

            class_item_starts = klass[1][10].split(', ')

            for item_name in class_item_starts:

                item = Item.objects.get(name=item_name)

                class_entry.starting_items.add(item)

            klass_features = klass[1][12].split(', ')

            for feature_name in klass_features:

                feature = Feature.objects.get(name=feature_name)

                class_entry.features.add(feature)

            klass_prestige = klass[1][13].split(', ')

            for prestige_name in klass_prestige:

                prestige = PrestigeClass.objects.get(name=prestige_name)

                class_entry.prestige_classes.add(prestige)
