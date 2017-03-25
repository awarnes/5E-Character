"""Single command to call all other populate commands. This will require that all initial migrations have been made."""


# Django Imports:
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """
    Command to populate the database with all information stored in CSVs for 5th Edition DnD.
    """

    # args
    help = 'Will auto populate the database with all the base information from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        COMMANDS = [
            "populate_skills", "populate_languages", "populate_tools", "populate_items", "populate_damage_types",
            "populate_weapon_properties", "populate_weapons", "populate_armor", "populate_features_part_1", "populate_alignments",
            "populate_prestige_classes", "populate_subraces", "populate_classes", "populate_races", "populate_backgrounds",
            "populate_spells", "populate_conditions", "populate_mounts_and_vehicles", "populate_features_part_2",
            # "populate_personality_traits", "populate_ideals", "populate_bonds", "populate_flaws",
        ]

        for command in COMMANDS:
            print("Starting {} command...".format(command))
            try:
                call_command(command, *args, **kwargs)
            except Exception as e:
                print("Had error with {} command: {}".format(command, e))
            else:
                print("Completed {} command successfully!".format(command))
