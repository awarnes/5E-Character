from django.db import models
from accounts.models import Member
from rules.models import (Class, Race, Feature, Skill, Language, Condition, DamageType)


# Create your models here.

class Character(models.Model):
    """This is the infromation for a character."""

    username = models.ForeignKey(Member, related_name='characters')

    char_name = models.CharField(max_length=1024)

    char_age = models.SmallIntegerField()
    char_height = models.SmallIntegerField()
    char_weight = models.SmallIntegerField()
    char_skin_color = models.CharField(max_length=128)
    char_hair_color = models.CharField(max_length=128)

    char_classes = models.ManyToManyField(Class, related_name='characters', through=)

    char_race = models.ForeignKey(Race, related_name='characters')

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


    skills = models.ManyToManyField(Skill, related_name='characters')
    features = models.ManyToManyField(Feature, related_name='characters')

    condition = models.ManyToManyField(Condition, related_name='characters')

    def get_char_level(self):
        """
        Adds all class levels to get the character level.

        :returns an int()
        """

    def __str__(self):
        return self.char_name


