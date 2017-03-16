# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import Background, Feature
from equipment.models import Item, Tool, Weapon, Armor


class Command(BaseCommand):
    """Command to populate the database with all skills for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the base Backgrounds from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/5E Rules CSVs/Backgrounds-Table 1.csv') as f:
            backgrounds = pd.read_csv(f, delimiter=',')

        backgrounds = backgrounds.dropna()

        for background in backgrounds.iterrows():
            # import pdb;pdb.set_trace()

            background_entry = Background.objects.create(
                name=background[1][0],
                description=background[1][1],
                gold_start=background[1][4],
                specials=background[1][9],
                # suggested_personality_traits=background[1][10],
                # suggested_ideals=background[1][11],
                # suggested_bonds=background[1][12],
                # suggested_flaws=background[1][13],
            )

            # TODO: Fix suggested flaws etc for external DB and loader.

            background_features = background[1][3].split(', ')

            for feature_name in background_features:

                feature = Feature.objects.filter(name=feature_name)

                background_entry.features.add(feature[0])

            background_tool_starts = background[1][5].split(', ')

            for tool_name in background_tool_starts:

                tool = Tool.objects.filter(name=tool_name)

                background_entry.tool_starts.add(tool[0])

            background_weapon_starts = background[1][7].split(', ')

            for weapon_name in background_weapon_starts:

                weapon = Weapon.objects.filter(name=weapon_name)

                background_entry.weapon_starts.add(weapon[0])

            background_armor_starts = background[1][8].split(', ')

            for armor_name in background_armor_starts:

                armor = Armor.objects.filter(name=armor_name)

                background_entry.armor_starts.add(armor[0])

            background_item_starts = background[1][6].split(', ')

            for item_name in background_item_starts:

                item = Item.objects.filter(name=item_name)

                background_entry.item_starts.add(item[0])

