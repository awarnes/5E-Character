"""
These are the model definitions that deal with characters. The majority of the information that a user actually interacts
with is in these models or linked by these models.


"""

# Python Imports
import math

# Django Imports
from django.db import models
from django.utils.text import slugify


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

    username = models.ForeignKey('accounts.Member', related_name='characters', editable=False)

    accessed = models.DateTimeField(auto_now=True,)

    # Flair
    char_name = models.CharField(max_length=1024, blank=True, null=True,)
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
    char_classes = models.ManyToManyField('rules.Class', related_name='character_classes', through='ClassLevel', blank=True,)
    char_prestige_classes = models.ManyToManyField('rules.PrestigeClass', related_name='character_prestiges', blank=True,)
    char_race = models.ForeignKey('rules.Race', related_name='character_races', blank=True, null=True,)
    char_subrace = models.ForeignKey('rules.Subrace', related_name='character_subraces', blank=True, null=True)
    char_background = models.ForeignKey('rules.Background', related_name='character_backgrounds', blank=True, null=True)
    alignment = models.ForeignKey('rules.Alignment', related_name='character_alignments', blank=True, null=True,)
    char_xp = models.IntegerField(default=0, blank=True, null=True,)

    # Ability Scores
    STR_score = IntegerMinMaxField(min_value=1, max_value=20, blank=True, null=True,)
    DEX_score = IntegerMinMaxField(min_value=1, max_value=20, blank=True, null=True,)
    CON_score = IntegerMinMaxField(min_value=1, max_value=20, blank=True, null=True,)
    INT_score = IntegerMinMaxField(min_value=1, max_value=20, blank=True, null=True,)
    WIS_score = IntegerMinMaxField(min_value=1, max_value=20, blank=True, null=True,)
    CHA_score = IntegerMinMaxField(min_value=1, max_value=20, blank=True, null=True,)

    # Saving Throws
    STR_saving_throw = models.BooleanField(default=False)
    DEX_saving_throw = models.BooleanField(default=False)
    CON_saving_throw = models.BooleanField(default=False)
    INT_saving_throw = models.BooleanField(default=False)
    WIS_saving_throw = models.BooleanField(default=False)
    CHA_saving_throw = models.BooleanField(default=False)

    # Actions >> May not need to use if just pulling through races and etc.
    features = models.ManyToManyField('rules.Feature', related_name='character_features', blank=True,)

    # Combat
    conditions = models.ManyToManyField('rules.Condition', related_name='character_conditions', blank=True,)
    death_fails = models.SmallIntegerField(default=0)
    death_successes = models.SmallIntegerField(default=0)
    max_health = models.SmallIntegerField(default=0)
    current_health = models.SmallIntegerField(default=0)
    temp_addtl_hp = models.SmallIntegerField(default=0)
    speed = models.SmallIntegerField(default=30)
    inspiration = models.SmallIntegerField(blank=True, null=True,)

    # Spells
    spell_book = models.ManyToManyField('spells.Spell', related_name='character_spells', through='SpellsReady', blank=True,)

    # Inventory
    tools_inv = models.ManyToManyField('equipment.Tool', related_name='character_tools_inv', blank=True,)
    items_inv = models.ManyToManyField('equipment.Item', related_name='character_items_inv', blank=True,)
    armor_inv = models.ManyToManyField('equipment.Armor', related_name='character_armor_inv', blank=True,)
    weapons_inv = models.ManyToManyField('equipment.Weapon', related_name='character_weapons_inv', blank=True,)

    slug = models.SlugField(editable=False, blank=True, null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.char_name)
        super().save(*args, **kwargs)

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
            'STR': self.STR_score,
            'DEX': self.DEX_score,
            'CON': self.CON_score,
            'INT': self.INT_score,
            'WIS': self.WIS_score,
            'CHA': self.CHA_score,
        }

        return (score_conversion[ability] - 10) // 2

    def get_passive_score(self, ability):
        """
        Gets the passive check for a given ability score.
        :return: int()
        """

        return self.get_ability_bonus(ability) + 10

    def get_char_level(self):
        """
        Adds all class levels to get the character level.

        :return: an int()
        """

        class_levels = self.classlevels.all()

        level = 0

        for class_level in class_levels:
            level += class_level.class_level

        return level

    def get_initiative_bonus(self):
        """
        Returns the total initiative bonus for a character.
        :return: int()
        """

        initiative = 0
        if 'Alert' in self.features.all():  # TODO: May not work with feats once they're added in...
            initiative += 4 + self.get_ability_bonus('DEX')

        else:
            initiative += self.get_ability_bonus('DEX')

        return initiative

    def get_armor_class(self):
        """
        Returns the total armor class for a character.
        :return: int()
        """

        armors = self.armor_inv.all()

        armor_class = 0

        for armor in armors:
            armor_class += armor.base_armor_class
            if armor.dexterity_modifier is True and armor.dexterity_modifier_max == -1:
                    armor_class += self.get_ability_bonus('DEX')
            elif armor.dexterity_modifier == True:
                if self.get_ability_bonus('DEX') >= 2:
                    armor_class += 2
                else:
                    armor_class += self.get_ability_bonus('DEX')

        return armor_class

    def __str__(self):
        return self.char_name


class ClassLevel(models.Model):
    """Through table for class levels for a character."""

    character = models.ForeignKey('Character', related_name='classlevels')
    char_class = models.ForeignKey('rules.Class', related_name='classlevels')

    class_level = IntegerMinMaxField(min_value=1, max_value=20)

    def __str__(self):
        return self.character.char_name


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
