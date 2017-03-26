# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from equipment.models import MountAndVehicle


class Command(BaseCommand):
    """Command to populate the database with all spells for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the base Mounts and Vehicles from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Mounts and Vehicles-Table 1.csv') as f:
            mounts = pd.read_csv(f, delimiter=',')

        mounts = mounts.dropna()

        for mount in mounts.iterrows():

            mount_entry = MountAndVehicle(
                name=mount[1][0],
                item_type=mount[1][1],
                description=mount[1][2],
                weight=mount[1][3],
                material=mount[1][4],
                cost_copper=mount[1][5],
                cost_silver=mount[1][6],
                cost_gold=mount[1][7],
                cost_platinum=mount[1][8],
                special=mount[1][9],

                speed=mount[1][10],
                carrying_capacity=mount[1][11],
                vehicle_type=mount[1][12],

            )

            mount_entry.save()

