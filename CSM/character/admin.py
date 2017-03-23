# Django Imports:
from django.contrib import admin
from django import forms
from searchableselect.widgets import SearchableSelect

# Model Imports:
from .models import Character, ClassLevel, SpellsReady
from rules.models import Class


# class ClassesForm(forms.ModelForm):
#     class Meta:
#         model = Character
#         exclude = ()
#         widgets = {
#             'char_classes': SearchableSelect(model='rules.Class', search_field='name', many=True)
#         }
#
#
# class CharacterAdmin(admin.ModelAdmin):
#     """Custome model admin for characters."""
#
#     model = Character
#     list_display = ('char_name', 'username',)
#     form = ClassesForm

# Main Model:
admin.site.register(Character)

# Through Tables:
admin.site.register(ClassLevel)
admin.site.register(SpellsReady)
