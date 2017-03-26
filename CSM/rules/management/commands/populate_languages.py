# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import Language


class Command(BaseCommand):
    """Command to populate the database with all spells for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Languages from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Languages-Table 1.csv') as f:
            languages = pd.read_csv(f, delimiter=',')

        languages = languages.dropna()

        for language in languages.iterrows():

            language_entry = Language(
                name=language[1][0],
                description=language[1][1],
                typical_speakers=language[1][2],
                script=language[1][3],
            )

            language_entry.save()