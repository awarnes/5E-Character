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

        features_1 = features.ix[:, 'name':'ability_level']
        features_2 = features.ix[:, 'prereq_proficiency':'prereq_prestige_class']

        features = pd.concat([features_1, features_2], axis=1)

        features = features.dropna()

        for feature in features.iterrows():

            feature_entry = Feature(
                name=feature[1][0],
                description=feature[1][1],

                is_proficiency=feature[1][2],
                is_choice=feature[1][3],
                changes_at_level=feature[1][4],
                ability_level=feature[1][5],

                prereq_character_level = feature[1][7],
                prereq_class_level = feature[1][9],


            )

            feature_entry.save()
