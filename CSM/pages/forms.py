# Django Imports:
from django import forms

# Model Imports:
from rules.models import Race, Subrace, Class, Alignment, Background, PrestigeClass, Condition
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

    Strength = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable', 'readonly': 'true'}))
    Dexterity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable', 'readonly': 'true'}))
    Constitution = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable', 'readonly': 'true'}))
    Intelligence = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable', 'readonly': 'true'}))
    Wisdom = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable', 'readonly': 'true'}))
    Charisma = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable', 'readonly': 'true'}))


class CCRace(forms.Form):
    """Choose a race."""

    race = forms.ModelChoiceField(queryset=Race.objects.all())

    subrace = forms.ModelChoiceField(queryset=Subrace.objects.all())


class CCClass(forms.Form):
    """Choose a class."""

    klass = forms.ModelChoiceField(queryset=Class.objects.all())
    cleric_prestige = forms.ModelChoiceField(queryset=Class.objects.get(name='Cleric').prestige_classes.all(), required=False)
    sorcerer_prestige = forms.ModelChoiceField(queryset=Class.objects.get(name='Sorcerer').prestige_classes.all(), required=False)
    warlock_prestige = forms.ModelChoiceField(queryset=Class.objects.get(name='Warlock').prestige_classes.all(), required=False)
    hp = forms.IntegerField()


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
    armor = forms.ModelMultipleChoiceField(queryset=Armor.objects.all(), required=False)
    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), required=False)
    tools = forms.ModelMultipleChoiceField(queryset=Tool.objects.all(), required=False)


class NCResolve(forms.Form):
    """Final form for new character creation."""

    next_page = forms.CharField(max_length=128, widget=forms.TextInput, required=False)




class ChoiceForm(forms.Form):
    """Allows user to assign features with the is_choice=True field to their character."""

    feature_type = forms.CharField(max_length=1024, widget=forms.HiddenInput)
    redirect_page = forms.CharField(max_length=256, widget=forms.HiddenInput)
    max_choices = forms.IntegerField(min_value=1, widget=forms.HiddenInput)
    min_choices = forms.IntegerField(min_value=1, widget=forms.HiddenInput)

    feature_name = forms.CharField(max_length=128,)
    feature_choices = forms.ModelMultipleChoiceField(queryset=None, required=True,)

    # def clean(self):
    #     cleaned_data = super().clean()
    #
    #     value = cleaned_data['feature_choices']
    #
    #     if value > cleaned_data['max_choices']:
    #         raise forms.ValidationError(_("You cannot select more than {} items.".format(cleaned_data['max_choices'])), code='invalid')
    #     elif value < cleaned_data['min_choices']:
    #         raise forms.ValidationError(_("You must select at least {} items.".format(cleaned_data['min_choices'])), code='invalid')
    #     else:
    #         return cleaned_data

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        choices = self.initial.get('choices')
        self.fields['queryset'] = choices

        self.fields['feature_choices'].queryset = choices

        # models = kwargs.pop('models')

class BattleSheet(forms.Form):
    """Form for the battle tab of the character sheet, used to help save any updated information."""


    # Ability Scores:
    STR = forms.IntegerField(required=False, disabled=True)
    DEX = forms.IntegerField(required=False, disabled=True)
    CON = forms.IntegerField(required=False, disabled=True)
    INT = forms.IntegerField(required=False, disabled=True)
    WIS = forms.IntegerField(required=False, disabled=True)
    CHA = forms.IntegerField(required=False, disabled=True)

    # Saving Throws:
    STR_ST = forms.BooleanField(required=False, disabled=True)
    DEX_ST = forms.BooleanField(required=False, disabled=True)
    CON_ST = forms.BooleanField(required=False, disabled=True)
    INT_ST = forms.BooleanField(required=False, disabled=True)
    WIS_ST = forms.BooleanField(required=False, disabled=True)
    CHA_ST = forms.BooleanField(required=False, disabled=True)

    # Skills:
    acrobatics = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'acrobatics'}))
    animal = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'animal'}))
    arcana = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'arcana'}))
    athletics = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'athletics'}))
    deception = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'deception'}))
    history = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'history'}))
    insight = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'insight'}))
    intimidation = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'intimidation'}))
    investigation = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'investigation'}))
    medicine = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'medicine'}))
    nature = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'nature'}))
    perception = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'perception'}))
    performance = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'performance'}))
    persuasion = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'persuasion'}))
    religion = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'religion'}))
    sleight = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'sleight'}))
    stealth = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'stealth'}))
    survival = forms.BooleanField(required=False, disabled=True, widget=forms.CheckboxInput(attrs={'data-skill': 'survival'}))

    # Armor and Movement:
    ac = forms.IntegerField(required=False, disabled=True)
    init = forms.IntegerField(required=False, disabled=True)
    speed = forms.IntegerField(required=False, disabled=True)

    # HP and Conditions:
    max_hp = forms.IntegerField(required=False, disabled=True)
    cur_hp = forms.IntegerField(required=False, disabled=True)
    temp_hp = forms.IntegerField(required=False, disabled=True)
    conditions = forms.ModelMultipleChoiceField(queryset=Condition.objects.all(), required=False, disabled=True)

    # Point Tracker:
    current_points = forms.IntegerField(required=False, disabled=True)
    max_points = forms.IntegerField(required=False, disabled=True)

    spell_slots_1 = forms.IntegerField(required=False, disabled=True)
    spell_slots_2 = forms.IntegerField(required=False, disabled=True)
    spell_slots_3 = forms.IntegerField(required=False, disabled=True)
    spell_slots_4 = forms.IntegerField(required=False, disabled=True)
    spell_slots_5 = forms.IntegerField(required=False, disabled=True)
    spell_slots_6 = forms.IntegerField(required=False, disabled=True)
    spell_slots_7 = forms.IntegerField(required=False, disabled=True)
    spell_slots_8 = forms.IntegerField(required=False, disabled=True)
    spell_slots_9 = forms.IntegerField(required=False, disabled=True)
