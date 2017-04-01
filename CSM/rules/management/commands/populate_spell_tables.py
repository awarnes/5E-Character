# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import SpellTable


class Command(BaseCommand):
    """Command to populate the database with all Spell Tables for 5th Edition."""

    # args
    help = 'Will auto populate the database with all the Spell Tables from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Spell Tables-Table 1.csv') as f:
            spell_tables = pd.read_csv(f, delimiter=',')

        spell_tables = spell_tables.dropna()

        for spell_table in spell_tables.iterrows():

            spell_table_entry = SpellTable.objects.create(
                name=spell_table[1][0],
                cantrips_known=spell_table[1][1],
                preparing_stat=spell_table[1][2],
                preparing_level_modifier=spell_table[1][3],
                spells_known=spell_table[1][4],
                level_1_slots=spell_table[1][5],
                level_2_slots=spell_table[1][6],
                level_3_slots=spell_table[1][7],
                level_4_slots=spell_table[1][8],
                level_5_slots=spell_table[1][9],
                level_6_slots=spell_table[1][10],
                level_7_slots=spell_table[1][11],
                level_8_slots=spell_table[1][12],
                level_9_slots=spell_table[1][13],
            )

