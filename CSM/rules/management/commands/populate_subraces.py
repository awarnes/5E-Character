# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import Subrace


class Command(BaseCommand):
    """Command to populate the database with all skills for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Classes from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/5E Rules CSVs/Subraces-Table 1.csv') as f:
            subraces = pd.read_csv(f, delimiter=',')

        subraces = subraces.dropna()

        for subrace in subraces.iterrows():

            subrace_entry = Subrace(
                name=subrace[1][0],
                description=subrace[1][1],
                ability_score_1=subrace[1][2],
                ability_score_1_bonus=subrace[1][3],
                ability_score_2=subrace[1][4],
                ability_score_2_bonus=subrace[1][5],
            )

            subrace_features = subrace[1][6].split(', ')

            for feature in subrace_features:
                subrace_entry.features.add(feature)

            subrace_tool_starts = subrace[1][7].split(', ')

            for tool in subrace_tool_starts:
                subrace_entry.subrace_tool_starts.add(tool)

            subrace_weapon_starts = subrace[1][8].split(', ')

            for weapon in subrace_weapon_starts:
                subrace_entry.subrace_weapon_starts.add(weapon)

            subrace_armor_starts = subrace[1][9].split(', ')

            for armor in subrace_armor_starts:
                subrace_entry.subrace_armor_starts.add(armor)

            subrace_item_starts = subrace[1][10].split(', ')

            for item in subrace_item_starts:
                subrace_entry.subrace_item_starts.add(item)

            subrace_entry.save()
