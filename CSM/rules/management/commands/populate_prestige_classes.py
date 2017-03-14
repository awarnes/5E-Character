# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import PrestigeClass


class Command(BaseCommand):
    """Command to populate the database with all skills for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Prestige Classes from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/5E Rules CSVs/Prestige Classes-Table 1.csv') as f:
            prestiges = pd.read_csv(f, delimiter=',')

        prestiges = prestiges.dropna()

        for prestige in prestiges.iterrows():

            prestige_entry = PrestigeClass(
                name=prestige[1][0],
                description=prestige[1][1],
            )

            # TODO: input the starting equipment and make sure it saves information.

            klass_features = prestige[1][2].split(', ')

            for feature in klass_features:
                prestige_entry.features.add(feature)

            prestige_entry.save()
