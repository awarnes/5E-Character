# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from equipment.models import Tool


class Command(BaseCommand):
    """Command to populate the database with all spells for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the base Tools from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Tools-Table 1.csv') as f:
            tools = pd.read_csv(f, delimiter=',')

        tools = tools.dropna()

        for tool in tools.iterrows():

            tool_entry = Tool(
                name=tool[1][0],
                item_type=tool[1][1],
                description=tool[1][2],
                weight=tool[1][3],
                material=tool[1][4],
                cost_copper=tool[1][5],
                cost_silver=tool[1][6],
                cost_gold=tool[1][7],
                cost_platinum=tool[1][8],
                special=tool[1][9],

                requires_proficiency=tool[1][10],
                tool_type=tool[1][11],
            )

            tool_entry.save()
