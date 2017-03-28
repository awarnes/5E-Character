# Django Imports:
from django.contrib import admin
from django import forms
from searchableselect.widgets import SearchableSelect

# Model Imports:
from .models import Character, ClassLevel, SpellsReady
from rules.models import Class
from .forms import ClassesForm



class CharacterAdmin(admin.ModelAdmin):
    """Custom model admin for characters."""

    model = Character
    exclude = ()
    list_display = ('char_name', 'username',)
    form = ClassesForm


# Main Model:
admin.site.register(Character, CharacterAdmin)

# Through Tables:
admin.site.register(ClassLevel)
admin.site.register(SpellsReady)
