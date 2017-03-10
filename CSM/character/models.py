import math

from django.db import models

# Create your models here.

class ClassLevel(models.Model):
    """Through table for class levels for a character."""

    character = models.ForeignKey(Character, related_name='classlevels')
    char_class = models.ForeignKey('rules.Class', related_name='classlevels')

    class_level = models.SmallIntegerField()


class SkillProficiency(models.Model):
    """Through table for if a character is proficient with a skill."""

    character = models.ForeignKey(Character, related_name='skillproficiencies')
    skills = models.ForeignKey('rules.Skill', related_name='skillproficiencies')

    proficient = models.BooleanField(default=False)


class SpellsReady(models.Model):
    """Through table to determine if a spell is just known, or known and ready."""

    character = models.ForeignKey(Character, related_name='spellsready')
    spells = models.ForeignKey('spells.Spell', related_name='spellsready')

    spell_ready = models.BooleanField(default=False)

class ToolProficiency(models.Model):
    """Through table to check for proficiency of a tool."""

    character = models.ForeignKey(Character, related_name='toolproficiencies')
    tool = models.ForeignKey('equipment.Tool', related_name='toolproficiencies')

    is_proficient = models.BooleanField(default=False)

class Character(models.Model):
    """This is the information for a character."""

    username = models.ForeignKey('accounts.Member', related_name='characters')

    char_name = models.CharField(max_length=1024)
    alignment = models.ForeignKey('rules.Alignment', related_name='characters')
    char_xp = models.IntegerField(default=0)

    char_age = models.SmallIntegerField()
    char_height = models.SmallIntegerField()
    char_weight = models.SmallIntegerField()
    char_skin_color = models.CharField(max_length=128)
    char_hair_color = models.CharField(max_length=128)
    char_eye_color = models.CharField(max_length=128)
    languages = models.ManyToManyField('rules.Language', related_name='characters')

    speed = models.SmallIntegerField()
    inspiration = models.SmallIntegerField()

    char_classes = models.ManyToManyField('rules.Class', related_name='characters', through=ClassLevel)

    char_race = models.ForeignKey('rules.Race', related_name='characters')

    STR_score = models.SmallIntegerField()
    DEX_score = models.SmallIntegerField()
    CON_score = models.SmallIntegerField()
    INT_score = models.SmallIntegerField()
    WIS_score = models.SmallIntegerField()
    CHA_score = models.SmallIntegerField()

    STR_saving_throw = models.BooleanField(default=False)
    DEX_saving_throw = models.BooleanField(default=False)
    CON_saving_throw = models.BooleanField(default=False)
    INT_saving_throw = models.BooleanField(default=False)
    WIS_saving_throw = models.BooleanField(default=False)
    CHA_saving_throw = models.BooleanField(default=False)

    skills = models.ManyToManyField('rules.Skill', related_name='characters', through=SkillProficiency)
    features = models.ManyToManyField('rules.Feature', related_name='characters')

    conditions = models.ManyToManyField('rules.Condition', related_name='characters')
    death_saves = models.SmallIntegerField(default=3)
    max_health = models.SmallIntegerField()
    current_health = models.SmallIntegerField()

    spell_book = models.ManyToManyField('spells.Spell', related_name='characters', through=SpellsReady)

    tools = models.ManyToManyField('equipment.Tools', related_name='characters', through=ToolProficiency)
    items = models.ManyToManyField('equipment.Item', related_name='characters')
    armor = models.ManyToManyField('equipment.Armor', related_name='characters', through=ArmorProficiency)
    weapons = models.ManyToManyField('equipment.Weapon', related_name='characters', through=WeaponProficiency)


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
