"""
Custom Template Tags for the Character Model. General use is to invoke functions that require more than one arg.
"""

from django import template


register = template.Library()


@register.simple_tag()
def ab_bonus(character, ability):
    return character.get_ability_bonus(ability)


@register.simple_tag()
def passive_bonus(character, ability):
    return character.get_passive_score(ability)