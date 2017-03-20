# Django Imports:
from django import forms


class SearchDatabase(forms.Form):
    """Provides an interface to search the database with."""

    query = forms.CharField(max_length=256, label='Search')

# class CharacterCreationGuided(forms.Form):
#     """Does the member want help with creating their character, or do they want to do free-for-all?"""
#
#     guided = forms.BooleanField(widget=forms.Select)


class AbilityScoresChoice(forms.Form):
    """Setting ability scores."""

    Strength = forms.IntegerField()
    Dexterity = forms.IntegerField()
    Constitution = forms.IntegerField()
    Intelligence = forms.IntegerField()
    Wisdom = forms.IntegerField()
    Charisma = forms.IntegerField()

class AbilityScoresBuy(forms.Form):
    """Setting ability scores."""


class AbilityScoresRoll(forms.Form):
    """Setting ability scores."""


class CharacterCreationName(forms.Form):
    """Start character creation with a name."""
    # TODO: May need some validation that it's not the same as another character, and if is add a secret name to differentiate.

    name = forms.CharField(max_length=512)
