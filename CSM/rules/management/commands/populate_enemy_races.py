# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import EnemyRace


class Command(BaseCommand):
    """Command to populate the database with all Enemy Races for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Enemy Races from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Enemy Races-Table 1.csv') as f:
            races = pd.read_csv(f, delimiter=',')

        races = races.dropna()

        for race in races.iterrows():

            EnemyRace.objects.create(
                name=race[1][0],
                description=race[1][1],
                usual_location=race[1][2],
            )