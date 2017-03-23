# Django Imports:
from django.contrib import admin

# Model Imports:
from .models import Character, ClassLevel, SpellsReady
from rules.models import Class


class ClassesInline(admin.TabularInline):

    model = ClassLevel
    extra = 0


class CharacterAdmin(admin.ModelAdmin):
    """Custome model admin for characters."""

    model = Character
    list_display = ('char_name', 'username',)
    # inlines = ['char_classes']
    list_filter = ('char_name', 'username', )

# Main Model:
admin.site.register(Character, CharacterAdmin)

# Through Tables:
admin.site.register(ClassLevel)
admin.site.register(SpellsReady)
