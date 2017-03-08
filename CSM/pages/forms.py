from django import forms

from spells.models import Spell


class SearchSpells(forms.Form):
    """Allows the user to search for spells."""
    query = forms.CharField(max_length=256)