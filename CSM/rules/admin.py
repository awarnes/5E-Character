# Django Imports
from django.contrib import admin

# Model Imports:
from .models import Subrace, Race, PrestigeClass, Class, Background, PersonalityTrait, Ideal, Bond, Flaw, Alignment
from .models import Feature, Skill, Language, DamageType, Condition, DragonAncestry, LandType, EnemyRace, Action, SpellTable


# Main information:
admin.site.register(Subrace)
admin.site.register(Race)
admin.site.register(PrestigeClass)
admin.site.register(Class)
admin.site.register(Background)
admin.site.register(SpellTable)

# Flair
admin.site.register(PersonalityTrait)
admin.site.register(Ideal)
admin.site.register(Bond)
admin.site.register(Flaw)
admin.site.register(Alignment)

# Skills and Features
admin.site.register(Feature)
admin.site.register(Skill)
admin.site.register(Language)

# Base Rules
admin.site.register(DamageType)
admin.site.register(Condition)
admin.site.register(DragonAncestry)
admin.site.register(EnemyRace)
admin.site.register(LandType)
admin.site.register(Action)
