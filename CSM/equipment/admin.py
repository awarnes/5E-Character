from django.contrib import admin

from .models import Weapon, WeaponProperty
# Register your models here.

admin.site.register(Weapon)
admin.site.register(WeaponProperty)
