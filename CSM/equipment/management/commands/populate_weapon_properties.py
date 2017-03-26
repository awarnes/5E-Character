# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from equipment.models import WeaponProperty


class Command(BaseCommand):
    """Command to populate the database with all Weapon Properties for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the base Weapon Properties from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Weapon Properties-Table 1.csv') as f:
            properties = pd.read_csv(f, delimiter=',')

        properties = properties.dropna()

        for property in properties.iterrows():

            property_entry = WeaponProperty(
                name=property[1][0],
                description=property[1][1],
            )

            property_entry.save()
