# Django Imports:
from django import forms

# Model Imports:
from rules.models import Race, Subrace, Class, Alignment, Background, PrestigeClass
from equipment.models import Weapon, Armor, Item, Tool


class SearchDatabase(forms.Form):
    """Provides an interface to search the database with."""

    query = forms.CharField(max_length=256, label='Search')

# class CharacterCreationGuided(forms.Form):
#     """Does the member want help with creating their character, or do they want to do free-for-all?"""
#
#     guided = forms.BooleanField(widget=forms.Select)


class AbilityScoresChoice(forms.Form):
    """Setting ability scores."""

    Strength = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable'}))
    Dexterity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable'}))
    Constitution = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable'}))
    Intelligence = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable'}))
    Wisdom = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable'}))
    Charisma = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable'}))


class CCRace(forms.Form):
    """Choose a race."""

    race = forms.ModelChoiceField(queryset=Race.objects.all())

    subrace = forms.ModelChoiceField(queryset=Subrace.objects.all())


class CCClass(forms.Form):
    """Choose a class."""

    klass = forms.ModelChoiceField(queryset=Class.objects.all())
    prestige = forms.ModelChoiceField(queryset=PrestigeClass.objects.all())


class CCPersonality(forms.Form):
    """Choose an alignment."""

    alignment = forms.ModelChoiceField(queryset=Alignment.objects.all())
    ideals = forms.CharField(widget=forms.Textarea, required=False)
    bonds = forms.CharField(widget=forms.Textarea, required=False)
    flaws = forms.CharField(widget=forms.Textarea, required=False)


class CCBackground(forms.Form):
    """Choose a background."""

    background = forms.ModelChoiceField(queryset=Background.objects.all())


class CCEquipment(forms.Form):
    """Choose equipment."""

    weapons = forms.ModelMultipleChoiceField(queryset=Weapon.objects.all(), required=False)
    armor = forms.ModelChoiceField(queryset=Armor.objects.all(), required=False)
    items = forms.ModelChoiceField(queryset=Item.objects.all(), required=False)
    tools = forms.ModelChoiceField(queryset=Tool.objects.all(), required=False)


