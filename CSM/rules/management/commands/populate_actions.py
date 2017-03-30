# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import Action


class Command(BaseCommand):
    """Command to populate the database with all Actions for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Actions from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Actions-Table 1.csv') as f:
            actions = pd.read_csv(f, delimiter=',')

        actions = actions.dropna()

        for action in actions.iterrows():

            Action.objects.create(
                name=action[1][0],
                description=action[1][1],
                is_base=action[1][2],
                base_action_type=action[1][3],
            )