# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from rules.models import Feature, Class, PrestigeClass


class Command(BaseCommand):
    """Command to populate the database with feature fields dependant on other models for 5th Edition."""

    # args
    help = 'Will auto populate the database with feature fields dependant on other models from 5th Edition Dungeons and Dragons.'

    def handle(self, *args, **kwargs):

        with open('/Users/alexanderwarnes/Documents/abw_codes/Git/5E Rules CSVs/5E Rules CSVs/Features-Table 1.csv') as f:
            features = pd.read_csv(f, delimiter=',')

        features_1 = features.ix[:, 'name':'ability_level']
        features_2 = features.ix[:, 'prereq_proficiency':'prereq_prestige_class']

        features = pd.concat([features_1, features_2], axis=1)

        features = features.dropna()

        for feature in features.iterrows():

            feature_name = feature[1][0]

            feature_entry = Feature.objects.get(name__iexact=feature_name)

            try:

                prof_names = feature[1][6].split(', ')

                for name in prof_names:

                    prof = Feature.objects.get(name__iexact=name)

                    feature_entry.prereq_proficiency.add(prof)

            except:
                print('fail prof {}'.format(prof))


            try:

                class_name = feature[1][8]

                klass = Class.objects.get(name__iexact=class_name)

                feature_entry.prereq_class = klass

                feature_entry.save()

            except:
                if class_name != 'None':
                    print('fail class {}, {}'.format(class_name, feature_name))


            try:

                prestige_name = feature[1][10]

                prestige = PrestigeClass.objects.get(name__iexact=prestige_name)

                feature_entry.prereq_prestige_class = prestige

                feature_entry.save()
            except:
                if prestige_name != 'None':
                    print('fail prestige {}, {}'.format(prestige_name, feature_name))


