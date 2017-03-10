# Django Imports:
from django.contrib import admin

# Model Imports:
from .models import Item, Weapon, Armor, Tool, EquipmentBonus, WeaponProperty


# Main Model:
admin.site.register(Item)

# Supplementary Models:
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(Tool)

# Modifying Models:
admin.site.register(EquipmentBonus)
admin.site.register(WeaponProperty)


