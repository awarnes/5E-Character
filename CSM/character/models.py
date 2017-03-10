"""
These are the model definitions that deal with characters. The majority of the information that a user actually interacts
with is in these models or linked by these models.


"""

# Python Imports
import math

# Django Imports
from django.db import models


class IntegerMinMaxField(models.IntegerField):
    """
    A field that only allows values between the specified minimum and maximum values.
    """

    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if (self.min_value is not None) and (self.max_value is not None):
            kwargs['min_value'] = self.min_value
            kwargs['max_value'] = self.max_value

        return name, path, args, kwargs

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super().formfield(**defaults)


class Character(models.Model):
    """
    This is the information for a character.

    ***NOTE: This is the specific model a Member will be interacting with the most.***
    """

    username = models.ForeignKey('accounts.Member', related_name='characters')

    # Flair
    char_name = models.CharField(max_length=1024)
    description = models.TextField(blank=True, null=True,)

    portrait = models.ImageField(blank=True, null=True,)
    char_age = models.SmallIntegerField(blank=True, null=True,)
    char_height = models.SmallIntegerField(blank=True, null=True,)
    char_weight = models.SmallIntegerField(blank=True, null=True,)
    char_skin_color = models.CharField(max_length=128, blank=True, null=True,)
    char_hair_color = models.CharField(max_length=128, blank=True, null=True,)
    char_eye_color = models.CharField(max_length=128, blank=True, null=True,)

    personality = models.TextField(blank=True, null=True,)
    ideals = models.TextField(blank=True, null=True,)
    bonds = models.TextField(blank=True, null=True,)
    flaws = models.TextField(blank=True, null=True,)

    allies = models.CharField(max_length=512, blank=True, null=True,)
    organizations = models.CharField(max_length=512, blank=True, null=True,)

    # languages = models.ManyToManyField('rules.Language', related_name='characters')

    # Basics
    char_classes = models.ManyToManyField('rules.Class', related_name='characters', through='ClassLevel')
    char_race = models.ForeignKey('rules.Race', related_name='characters')
    char_background = models.ForeignKey('rules.Background', related_name='characters')
    alignment = models.ForeignKey('rules.Alignment', related_name='character_alignments')
    char_xp = models.IntegerField(default=0, blank=True, null=True,)

    # Ability Scores
    STR_score = IntegerMinMaxField(min_value=1, max_value=20)
    DEX_score = IntegerMinMaxField(min_value=1, max_value=20)
    CON_score = IntegerMinMaxField(min_value=1, max_value=20)
    INT_score = IntegerMinMaxField(min_value=1, max_value=20)
    WIS_score = IntegerMinMaxField(min_value=1, max_value=20)
    CHA_score = IntegerMinMaxField(min_value=1, max_value=20)

    # Saving Throws
    STR_saving_throw = models.BooleanField(default=False)
    DEX_saving_throw = models.BooleanField(default=False)
    CON_saving_throw = models.BooleanField(default=False)
    INT_saving_throw = models.BooleanField(default=False)
    WIS_saving_throw = models.BooleanField(default=False)
    CHA_saving_throw = models.BooleanField(default=False)

    # Actions >> May not need to use if just pulling through races and etc.
    features = models.ManyToManyField('rules.Feature', related_name='character_features')

    # # Proficiencies >> Comes from features through classes, prestige classes, races, or subraces now.
    # skills_prof = models.ManyToManyField('rules.Skill', related_name='character_skill_profs')  # may use through=SkillProficiency
    # tools_prof = models.ManyToManyField('equipment.Tool', related_name='character_tool_profs', blank=True, null=True,)
    # armor_prof = models.ManyToManyField('equipment.Armor', related_name='character_armor_profs', blank=True, null=True,)
    # weapons_prof = models.ManyToManyField('equipment.Weapon', related_name='character_weapon_profs', blank=True, null=True,)

    # Combat
    conditions = models.ManyToManyField('rules.Condition', related_name='character_conditions', blank=True,)
    death_fails = models.SmallIntegerField(default=0)
    death_successes = models.SmallIntegerField(default=0)
    max_health = models.SmallIntegerField()
    current_health = models.SmallIntegerField()
    temp_addtl_hp = models.SmallIntegerField()
    speed = models.SmallIntegerField()
    inspiration = models.SmallIntegerField(blank=True, null=True,)

    # Spells
    spell_book = models.ManyToManyField('spells.Spell', related_name='character_spells', through='SpellsReady', blank=True,)

    # Inventory
    tools_inv = models.ManyToManyField('equipment.Tool', related_name='character_tools_inv', blank=True,)
    items_inv = models.ManyToManyField('equipment.Item', related_name='character_items_inv', blank=True,)
    armor_inv = models.ManyToManyField('equipment.Armor', related_name='character_armor_inv', blank=True,)
    weapons_inv = models.ManyToManyField('equipment.Weapon', related_name='character_weapons_inv', blank=True,)

    def get_prof_bonus(self):
        """
        Gets the proficiency bonus for a character based on their character level.
        :return: int()
        """

        return int(math.ceil(self.get_char_level() / 4) + 1)

    def get_ability_bonus(self, ability):
        """
        Gets the bonus for a given ability score.
        :return: int()
        """

        score_conversion = {
            'Strength': self.STR_score,
            'Dexterity': self.DEX_score,
            'Constitution': self.CON_score,
            'Intelligence': self.INT_score,
            'Wisdom': self.WIS_score,
            'Charisma': self.CHA_score,
        }

        return (score_conversion[ability] - 10) // 2

    def get_passive_score(self, ability):
        """
        Gets the passive check for a given ability score.
        :return: int()
        """

        score_conversion = {
            'Strength': self.STR_score,
            'Dexterity': self.DEX_score,
            'Constitution': self.CON_score,
            'Intelligence': self.INT_score,
            'Wisdom': self.WIS_score,
            'Charisma': self.CHA_score,
        }

        return self.get_ability_bonus(score_conversion[ability]) + 10

    def get_char_level(self):
        """
        Adds all class levels to get the character level.

        :return: an int()
        """

        # TODO: get information from through table: ClassLevels

        return 1

    def get_initiative_bonus(self):
        """
        Returns the total initiative bonus for a character.
        :return: int()
        """

        # TODO: interact with features, current dexterity to total intitiative bonus.

    def get_armor_class(self):
        """
        Returns the total armor class for a character.
        :return: int()
        """

        # TODO: interact with inventory, current dexterity to get total AC.

    def __str__(self):
        return self.char_name


class ClassLevel(models.Model):
    """Through table for class levels for a character."""

    character = models.ForeignKey('Character', related_name='classlevels')
    char_class = models.ForeignKey('rules.Class', related_name='classlevels')

    class_level = IntegerMinMaxField(min_value=1, max_value=20)

    def __str__(self):
        return self.character


class SpellsReady(models.Model):
    """Through table to determine if a spell is just known, or known and ready."""

    character = models.ForeignKey('Character', related_name='spellsready')
    spells = models.ForeignKey('spells.Spell', related_name='spellsready')

    spell_ready = models.BooleanField(default=False)

    def __str__(self):
        return self.character

    class Meta:
        verbose_name = "Spell Ready"
        verbose_name_plural = "Spells Ready"


# May not need to use this through table, as all skills a character has they will be proficient in.
# if they don't have the skill, the calculation will just add normal results w/o prof bonus
#
# class SkillProficiency(models.Model):
#     """Through table for if a character is proficient with a skill."""
#
#     character = models.ForeignKey(Character, related_name='skillproficiencies')
#     skills = models.ForeignKey('rules.Skill', related_name='skillproficiencies')
#
#     proficient = models.BooleanField(default=False)

#
# class ToolProficiency(models.Model):
#     """Through table to check for proficiency of a tool."""
#
#     character = models.ForeignKey(Character, related_name='toolproficiencies')
#     tool = models.ForeignKey('equipment.Tool', related_name='toolproficiencies')
#
#     is_proficient = models.BooleanField(default=False)
#
#
# class ArmorProficiency(models.Model):
#     """Through table to check for proficiency of a tool."""
#
#     character = models.ForeignKey(Character, related_name='armorproficiencies')
#     armor = models.ForeignKey('equipment.Armor', related_name='armorproficiencies')
#
#     is_proficient = models.BooleanField(default=False)
#
#
# class WeaponProficiency(models.Model):
#     """Through table to check for proficiency of a tool."""
#
#     character = models.ForeignKey(Character, related_name='weaponproficiencies')
#     weapon = models.ForeignKey('equipment.Weapon', related_name='weaponproficiencies')
#
#     is_proficient = models.BooleanField(default=False)