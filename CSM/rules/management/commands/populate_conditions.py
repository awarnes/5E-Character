# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import Condition


class Command(BaseCommand):
    """Command to populate the database with all spells for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Conditions from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/5E Rules CSVs/Conditions-Table 1.csv') as f:
            conditions = pd.read_csv(f, delimiter=',')

        # features = features.ix[:,'name':'description':'associated_ability':'example_tasks']

        conditions = conditions.dropna()

        for condition in conditions.iterrows():

            condition_entry = Condition(
                name=condition[1][0],
                description=condition[1][1],
            )

            condition_entry.save()
