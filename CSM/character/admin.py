# Django Imports:
from django.contrib import admin

# Model Imports:
from .models import Character, ClassLevel, SpellsReady


# Main Model:
admin.site.register(Character)

# Through Tables:
admin.site.register(ClassLevel)
admin.site.register(SpellsReady)
