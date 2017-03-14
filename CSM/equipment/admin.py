# Django Imports:
from django.contrib import admin

# Model Imports:
from .models import Equipment, Item, Weapon, Armor, Tool, EquipmentBonus, WeaponProperty


# Main Model:
admin.site.register(Equipment)

# Supplementary Models:
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(Tool)
admin.site.register(Item)

# Modifying Models:
admin.site.register(EquipmentBonus)
admin.site.register(WeaponProperty)


