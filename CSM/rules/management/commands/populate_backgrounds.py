# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import Background


class Command(BaseCommand):
    """Command to populate the database with all skills for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the base Backgrounds from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/5E Rules CSVs/Backgrounds-Table 1.csv') as f:
            backgrounds = pd.read_csv(f, delimiter=',')

        backgrounds = backgrounds.dropna()

        for background in backgrounds.iterrows():

            background_entry = Background(
                name=background[1][0],
                description=background[1][1],
                languages=background[1][2],
                gold_start=background[1][4],
                special=background[1][9],
                suggested_personality_traits=background[1][10],
                suggested_ideals=background[1][11],
                suggested_bonds=background[1][12],
                suggested_flaws=background[1][13],
            )

            # TODO: Fix suggested flaws etc for external DB and loader.

            background_features = background[1][3].split(', ')

            for feature in background_features:
                background_entry.features.add(feature)

            background_tool_starts = background[1][5].split(', ')

            for tool in background_tool_starts:
                background_entry.subrace_tool_starts.add(tool)

            background_weapon_starts = background[1][7].split(', ')

            for weapon in background_weapon_starts:
                background_entry.subrace_weapon_starts.add(weapon)

            background_armor_starts = background[1][8].split(', ')

            for armor in background_armor_starts:
                background_entry.subrace_armor_starts.add(armor)

            background_item_starts = background[1][6].split(', ')

            for item in background_item_starts:
                background_entry.subrace_item_starts.add(item)

            background_entry.save()
