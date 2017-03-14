# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import Race


class Command(BaseCommand):
    """Command to populate the database with all skills for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Classes from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/5E Rules CSVs/Races-Table 1.csv') as f:
            races = pd.read_csv(f, delimiter=',')

        races = races.dropna()

        for race in races.iterrows():

            race_entry = Race(
                name=race[1][0],
                description=race[1][1],
                ability_score_1=race[1][2],
                ability_score_1_bonus=race[1][3],
                ability_score_2=race[1][4],
                ability_score_2_bonus=race[1][5],
                age_adult=race[1][6],
                age_mortality=race[1][7],
                typical_alignment=race[1][8],
                size=race[1][9],
                typical_height_min=race[1][10],
                typical_height_max=race[1][11],
                typical_weight_min=race[1][12],
                typical_weight_max=race[1][13],
                speed=race[1][14],
                speed_special=race[1][15],
            )

            race_features = race[1][16].split(', ')

            for feature in race_features:
                race_entry.features.add(feature)

            race_tool_starts = race[1][17].split(', ')

            for tool in race_tool_starts:
                race_entry.race_tool_starts.add(tool)

            race_weapon_starts = race[1][18].split(', ')

            for weapon in race_weapon_starts:
                race_entry.race_weapon_starts.add(weapon)

            race_armor_starts = race[1][19].split(', ')

            for armor in race_armor_starts:
                race_entry.race_armor_starts.add(armor)

            race_item_starts = race[1][20].split(', ')

            for item in race_item_starts:
                race_entry.race_item_starts.add(item)

            race_subraces = race[1][21].split(', ')

            for subrace in race_subraces:
                race_entry.subraces.add(subrace)

            race_entry.save()