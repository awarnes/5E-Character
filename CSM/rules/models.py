from django.db import models

# Create your models here.

class Race(models.Model):
    """Information about races in D&D"""

    # name
    # description
    # suggested_first_names
    # suggested_last_names
    #
    # ability_score_increase
    # age_range
    # typical_alignment
    # size
    # typical_height
    # typical_weight
    # speed
    # speed_special
    # special_abilities = models.ManyToManyField()
    # proficiencies
    # languages
    # subraces


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
    """Information about race, class, subrace, subclass, and background features."""

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

    weapon_proficiency = models.ManyToManyField(Weapon, related_query_name='feature', blank=True, null=True)
    armor_proficiency = models.ManyToManyField(Armor, related_query_name='feature', blank=True, null=True)
    tool_proficiency = models.ManyToManyField(Tool, related_query_name='feature', blank=True, null=True)
    skill_proficiency = models.ManyToManyField(Skill, related_query_name='feature', blank=True, null=True)
    languages_known = models.ManyToManyField(Language, related_query_name='feature', blank=True, null=True)

    spell_choice = models.ManyToManyField(Spell, related_query_name='feature', blank=True, null=True)
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
