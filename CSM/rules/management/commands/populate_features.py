# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import Feature


class Command(BaseCommand):
    """Command to populate the database with all spells for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Features from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/5E Rules CSVs/Features-Table 1.csv') as f:
            features = pd.read_csv(f, delimiter=',')

        features = features.ix[:,'Name':'Description']

        features = features.dropna()

        for feature in features.iterrows():

            feature_entry = Feature(
                name=feature[1][0],
                description=feature[1][1],
            )

            feature_entry.save()
