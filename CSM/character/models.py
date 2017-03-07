from django.db import models

# Create your models here.

class Character(models.Model):
    """This is the infromation for a character."""

    # player
    #
    # char_name
    #
    # char_classes
    # char_race
    # ability_scores
    # saving_throws
    # skills
    # char_level
    # char_prof


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
    # special_abilities
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

class Feat(models.Model):
    """Information about feats."""

    # name
    # description
    # prerequisite


class Feature(models.Model):
    """Information about race, class, subrace, subclass, and background features."""

    # name
    # description
    # options
    # uses

class Proficiency(models.Model):
    """Skill, equipment, and savings throw proficiencies."""

    # name
    # prof_type
    # ability
