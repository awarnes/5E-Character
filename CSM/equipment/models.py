"""
Models for all equipment in the game.
"""

# Django Imports
from django.db import models

# Module Imports
from character.models import IntegerMinMaxField


class WeaponProperty(models.Model):
    """The properties of weapons. Pages 146 and 147 of the PHB."""

    name = models.CharField(max_length=100, unique=True, help_text='Name of the weapon property.')
    description = models.TextField(help_text='Full description of the weapon property.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Weapon Property'
        verbose_name_plural = 'Weapon Properties'


class Weapon(models.Model):
    """Contains information regarding all weapons in the world."""

    WEAPON_TYPE = [
        ('Simple', 'Simple'),
        ('Martial', 'Martial'),
    ]

    MELEE_RANGED = [
        ('Melee', 'Melee'),
        ('Ranged', 'Ranged'),
    ]

    name = models.CharField(max_length=100, unique=True, help_text='Name of the weapon.')
    weapon_type = models.CharField(max_length=16, choices=WEAPON_TYPE, help_text='False = Simple Weapon, True = Martial Weapon.')
    melee_or_ranged = models.CharField(max_length=16, choices=MELEE_RANGED, help_text='False = Melee Weapon, True = Ranged Weapon.')
    normal_range = models.SmallIntegerField(null=True, blank=True, help_text='If a ranged weapon, any attack over normal range is made at disadvantage.')
    max_range = models.SmallIntegerField(null=False, blank=True, help_text='Maximum range a weapon can attack.')

    cost_copper = models.SmallIntegerField(null=True, blank=True, help_text='Cost in copper pieces.')
    cost_silver = models.SmallIntegerField(null=True, blank=True, help_text='Cost in silver pieces.')
    cost_gold = models.SmallIntegerField(null=True, blank=True, help_text='Cost in gold pieces.')
    cost_platinum = models.SmallIntegerField(null=True, blank=True, help_text='Cost in platinum pieces.')

    damage_dice_number = models.SmallIntegerField(help_text='Ex: Xd6 + 1.')
    damage_dice_size = models.SmallIntegerField(help_text='Ex: 1dX + 1.')
    damage_dice_bonus = models.SmallIntegerField(blank=True, null=True, help_text='Ex: 1d6 + X.')

    damage_type = models.ManyToManyField('rules.DamageType', related_name='weapons', help_text='What kind of damage is done by the weapon.')
    weight = models.SmallIntegerField(help_text='Carrying weight of the weapon.')
    properties = models.ManyToManyField(WeaponProperty, related_name='weapons')
    description = models.TextField(help_text='Full description of the weapon.')
    special = models.CharField(max_length=100, blank=True, null=True, help_text='General field for additional rules.')

    def __str__(self):
        return self.name


class Armor(models.Model):
    """Contains information regarding armor in the world."""

    ARMOR_TYPES = [
        ('Heavy', 'Heavy Armor'),
        ('Medium', 'Medium Armor'),
        ('Light', 'Light Armor'),
        ('Shield', 'Shield'),
    ]

    name = models.CharField(max_length=100, unique=True, help_text='Name of the armor.')
    armor_type = models.CharField(max_length=16, choices=ARMOR_TYPES)
    description = models.CharField(max_length=1028)
    weight = models.SmallIntegerField()

    cost_copper = models.SmallIntegerField(null=True, blank=True, help_text='Cost in copper pieces.')
    cost_silver = models.SmallIntegerField(null=True, blank=True, help_text='Cost in silver pieces.')
    cost_gold = models.SmallIntegerField(null=True, blank=True, help_text='Cost in gold pieces.')
    cost_platinum = models.SmallIntegerField(null=True, blank=True, help_text='Cost in platinum pieces.')

    base_armor_class = models.SmallIntegerField(null=True, blank=True)
    bonus_armor_class = models.SmallIntegerField(null=True, blank=True)
    dexterity_modifier = models.BooleanField(default=True, null=True, blank=True,)
    dexterity_modifier_max = models.SmallIntegerField(null=True, blank=True,)

    don_time = models.SmallIntegerField()
    doff_time = models.SmallIntegerField()
    req_str = models.SmallIntegerField(null=True, blank=True,)
    stealth_disadvantage = models.BooleanField(default=False, null=True, blank=True,)

    special = models.CharField(max_length=1028, null=True, blank=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Armor'
        verbose_name_plural = 'Armor'


class Item(models.Model):
    """Contains information on other items in the world."""

    name = models.CharField(max_length=100, unique=True, help_text='Name of the item.')
    item_type = models.CharField(max_length=128)
    description = models.CharField(max_length=1028)

    weight = models.SmallIntegerField(null=True, blank=True,)
    uses = models.SmallIntegerField(null=True, blank=True,)
    space = models.SmallIntegerField(null=True, blank=True,)

    cost_copper = models.SmallIntegerField(null=True, blank=True, help_text='Cost in copper pieces.')
    cost_silver = models.SmallIntegerField(null=True, blank=True, help_text='Cost in silver pieces.')
    cost_gold = models.SmallIntegerField(null=True, blank=True, help_text='Cost in gold pieces.')
    cost_platinum = models.SmallIntegerField(null=True, blank=True, help_text='Cost in platinum pieces.')

    special = models.CharField(max_length=1028, null=True, blank=True,)

    def __str__(self):
        return self.name


class Tool(Item):
    """Subclass of items that are tools."""

    requires_proficiency = models.BooleanField(default=False)
    tool_type = models.CharField(max_length=128)


class EquipmentBonus(models.Model):
    """All possible bonuses a magic item can have."""

    name = models.CharField(max_length=100, unique=True, help_text='Name of the bonus.')
    description = models.CharField(max_length=1028)

    ability_score = models.CharField(max_length=16, null=True, blank=True,)
    ability_bonus = models.SmallIntegerField(null=True, blank=True,)

    damage_type = models.ForeignKey('rules.DamageType', related_name='equpmentbonuses', null=True, blank=True,)
    damage_bonus = models.SmallIntegerField(null=True, blank=True,)
    damage_dice_number = models.SmallIntegerField(null=True, blank=True,)
    damage_dice_size = models.SmallIntegerField(null=True, blank=True,)

    advantage = models.BooleanField(default=False, null=True, blank=True,)
    disadvantage = models.BooleanField(default=False, null=True, blank=True,)
    check = models.CharField(max_length=128, null=True, blank=True,)

    skill = models.ForeignKey('rules.Skill', related_name='equipmentbonuses', null=True, blank=True,)
    skill_bonus = models.SmallIntegerField(null=True, blank=True,)

    spell = models.ForeignKey('spells.Spell', related_name='equipmentbonuses', null=True, blank=True,)
    spell_bonus = models.CharField(max_length=128, null=True, blank=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipment Bonus'
        verbose_name_plural = 'Equipment Bonuses'
