"""
Models that describe the rules used by 5th Edition Dungeons and Dragons.

The goal is to make these loose enough to allow others to add new instances (such as classes),
but particular enough that the information will still be programmatically accessible for the actual CSM
"""


# Django imports.
from django.db import models


class Subrace(models.Model):
    """Subraces for races."""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1028)
    ability_score_1 = models.CharField(max_length=16)
    ability_score_1_bonus = models.SmallIntegerField(blank=True, null=True,)

    ability_score_2 = models.CharField(max_length=16, blank=True, null=True)
    ability_score_2_bonus = models.SmallIntegerField(blank=True, null=True,)

    features = models.ManyToManyField(Feature, related_name='races')

    skills = models.ManyToManyField(Skill, related_name='races')
    tools = models.ManyToManyField('equipment.Tool', related_name='races')
    weapons = models.ManyToManyField('equipment.Weapon', related_name='races')
    armor = models.ManyToManyField('equipment.Armor', related_name='races')
    languages = models.ManyToManyField(Language, related_name='races')



class Race(models.Model):
    """Information about races in D&D"""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=10000)

    # Would like to move these to another module.
    # suggested_first_names
    # suggested_last_names

    ability_score_1 = models.CharField(max_length=16)
    ability_score_1_bonus = models.SmallIntegerField(blank=True, null=True,)

    ability_score_2 = models.CharField(max_length=16, blank=True, null=True)
    ability_score_2_bonus = models.SmallIntegerField(blank=True, null=True,)

    age_adult = models.SmallIntegerField()
    age_mortality = models.SmallIntegerField()

    typical_alignment = models.ForeignKey(Alignment, related_name='races')

    size = models.CharField(max_length=16, choices=SIZES)
    typical_height_min = models.SmallIntegerField()
    typical_height_max = models.SmallIntegerField()
    typical_weight_min = models.SmallIntegerField()
    typical_weight_max = models.SmallIntegerField()
    speed = models.SmallIntegerField()
    speed_special = models.CharField(max_length=128)

    features = models.ManyToManyField(Feature, related_name='races')

    skills = models.ManyToManyField(Skill, related_name='races')
    tools = models.ManyToManyField('equipment.Tool', related_name='races')
    weapons = models.ManyToManyField('equipment.Weapon', related_name='races')
    armor = models.ManyToManyField('equipment.Armor', related_name='races')
    languages = models.ManyToManyField(Language, related_name='races')

    subraces = models.ManyToManyField(Subrace, related_name='races')


class Class(models.Model):
    """Information about classes."""

    # name
    # description
    # spell_caster
    # ritual_caster
    # spell_casting_ability
    # proficiencies
    # hit_die


class Feature(models.Model):
    """
    Information about race, class, subrace, subclass, and background features.

    This is one of the heaviest lifters in the database because it will describe all possible interactions a player
    can take, excepting spells and items.
    """

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=10000)

    # action
    # action_constraint_start
    # action_constraint_end
    # action_duration
    # action_uses_per_day
    # action_distance

    stat_to_change = models.CharField(max_length=64, blank=True, null=True)
    stat_change_amount = models.SmallIntegerField(blank=True, null=True)

    weapon_proficiency = models.ManyToManyField('equipment.Weapon', related_query_name='feature', blank=True, null=True)
    armor_proficiency = models.ManyToManyField('equipment.Armor', related_query_name='feature', blank=True, null=True)
    tool_proficiency = models.ManyToManyField('equipment.Tool', related_query_name='feature', blank=True, null=True)
    skill_proficiency = models.ManyToManyField(Skill, related_query_name='feature', blank=True, null=True)
    languages_known = models.ManyToManyField(Language, related_query_name='feature', blank=True, null=True)

    spell_choice = models.ManyToManyField('spells.Spell', related_query_name='feature', blank=True, null=True)
    spell_choice_constraint_number = models.SmallIntegerField(blank=True, null=True)
    spell_choice_constraint_use = models.CharField(max_length=512, blank=True, null=True)

    damage_type = models.ManyToManyField(DamageType, related_query_name='feature', blank=True, null=True)
    damage_dice_number = models.SmallIntegerField(blank=True, null=True)
    damage_dice_size = models.SmallIntegerField(blank=True, null=True)
    damage_dice_bonus = models.SmallIntegerField(blank=True, null=True)

    damage_resistance_type = models.ManyToManyField(DamageType, related_query_name='feature', blank=True, null=True)
    # spell_resistance
    condition_resistance = models.ManyToManyField(Condition, related_query_name='feature', blank=True, null=True)

    long_rest_duration = models.SmallIntegerField(blank=True, null=True)
    # change_at_level

    prereq_ability = models.CharField(max_length=64, blank=True, null=True)
    prereq_ability_score = models.SmallIntegerField(blank=True, null=True)
    prereq_skill = models.CharField(max_length=64, blank=True, null=True)
    prereq_character_level = models.SmallIntegerField(blank=True, null=True)
    prereq_class = models.CharField(max_length=64, blank=True, null=True)
    prereq_class_level = models.SmallIntegerField(blank=True, null=True)


class Background(models.Model):
    """
    The model for character backgrounds.
    """

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=10000)

    skills = models.ManyToManyField(Skill, related_name='backgrounds', blank=True, null=True)
    languages = models.ManyToManyField(Language, related_name='backgrounds', blank=True, null=True)
    tools = models.ManyToManyField('equipment.Tool', related_name='backgrounds', blank=True, null=True)
    items = models.ManyToManyField('equipment.Item', related_name='backgrounds', blank=True, null=True)
    weapons = models.ManyToManyField('equipment.Weapon', related_name='backgrounds', blank=True, null=True)
    armor = models.ManyToManyField('equipment.Armor', related_name='backgrounds', blank=True, null=True)
    feature = models.ForeignKey(Feature, related_name='backgrounds', blank=True, null=True)

    suggested_personality_traits = models.ManyToManyField(PersonalityTrait, related_name='backgrounds', blank=True, null=True)
    suggested_ideals = models.ManyToManyField(Ideal, related_name='backgrounds', blank=True, null=True)
    suggested_bonds = models.ManyToManyField(Bond, related_name='backgrounds', blank=True, null=True)
    suggested_flaws = models.ManyToManyField(Flaw, related_name='backgrounds', blank=True, null=True)


class Skill(models.Model):
    """Model for describing skills."""

    name = models.CharField(max_length=128)
    associated_ability = models.CharField(max_length=64)
    description = models.CharField(max_length=10000)
    example_tasks = models.CharField(max_length=512, blank=True, null=True)


class Language(models.Model):
    """Model for describing languages."""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=10000)
    typical_speakers = models.CharField(max_length=256)
    script = models.CharField(max_length=128, blank=True, null=True)


class DamageType(models.Model):
    """Model for types of damage."""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)


class Condition(models.Model):
    """Model for different conditions."""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)


class Alignment(models.Model):
    """Model for different Alignments."""

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1028)


class PersonalityTrait(models.Model):
    """Model for basic suggested personality traits."""

    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=1028)


class Ideal(models.Model):
    """Model for basic suggested ideals."""

    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=1028)


class Bond(models.Model):
    """Model for basic suggested bonds."""

    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=1028)


class Flaw(models.Model):
    """Model for basic suggested flaws."""

    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=1028)