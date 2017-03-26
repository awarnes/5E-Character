# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import Alignment


class Command(BaseCommand):
    """Command to populate the database with all spells for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Alignments from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Alignments-Table 1.csv') as f:
            alignments = pd.read_csv(f, delimiter=',')

        alignments = alignments.dropna()

        for alignment in alignments.iterrows():

            Alignment.objects.create(
                name=alignment[1][0],
                description=alignment[1][1],
            )