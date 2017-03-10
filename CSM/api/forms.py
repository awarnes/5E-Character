from django import forms

class SearchSpells(forms.Form):
    """Allows the user to search for spells."""
    query = forms.CharField(max_length=256)