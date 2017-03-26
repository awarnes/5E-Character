# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import Skill


class Command(BaseCommand):
    """Command to populate the database with all skills for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Skills from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Skills-Table 1.csv') as f:
            skills = pd.read_csv(f, delimiter=',')

        skills = skills.dropna()

        for skill in skills.iterrows():

            skill_entry = Skill(
                name=skill[1][0],
                description=skill[1][1],
                associated_ability=skill[1][2],
                example_tasks=skill[1][3],
            )

            skill_entry.save()