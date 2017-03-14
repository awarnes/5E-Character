"""
Models for all equipment in the game.
"""

# TODO: Add a new base class: Equipment and subclass rest off of that. Items are other things >> Armor is not an Item.

# Django Imports
from django.db import models


class Equipment(models.Model):
    """Base class for all things you could hold (or not) in 5E."""

    name = models.CharField(max_length=100, unique=True, help_text='Name of the item.')
    item_type = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)

    weight = models.SmallIntegerField(null=True, blank=True, )
    material = models.CharField(max_length=128)

    cost_copper = models.SmallIntegerField(null=True, blank=True, help_text='Cost in copper pieces.')
    cost_silver = models.SmallIntegerField(null=True, blank=True, help_text='Cost in silver pieces.')
    cost_gold = models.SmallIntegerField(null=True, blank=True, help_text='Cost in gold pieces.')
    cost_platinum = models.SmallIntegerField(null=True, blank=True, help_text='Cost in platinum pieces.')

    special = models.CharField(max_length=1024, null=True, blank=True,
                               help_text='General field for additional rules.', )

    def __str__(self):
        return self.name


class Item(Equipment):
    """Contains information on other items in the world."""

    uses = models.SmallIntegerField(null=True, blank=True,)
    space = models.CharField(null=True, blank=True, max_length=128)

    def __str__(self):
        return self.name


class WeaponProperty(models.Model):
    """The properties of weapons. Pages 146 and 147 of the PHB."""

    name = models.CharField(max_length=100, unique=True, help_text='Name of the weapon property.')
    description = models.TextField(help_text='Full description of the weapon property.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Weapon Property'
        verbose_name_plural = 'Weapon Properties'


class Weapon(Equipment):
    """Contains information regarding all weapons in the world."""

    WEAPON_TYPE = [
        ('Simple', 'Simple'),
        ('Martial', 'Martial'),
    ]

    MELEE_RANGED = [
        ('Melee', 'Melee'),
        ('Ranged', 'Ranged'),
    ]

    weapon_type = models.CharField(max_length=16, choices=WEAPON_TYPE, help_text='False = Simple Weapon, True = Martial Weapon.')
    melee_or_ranged = models.CharField(max_length=16, choices=MELEE_RANGED, help_text='False = Melee Weapon, True = Ranged Weapon.')
    normal_range = models.SmallIntegerField(null=True, blank=True, help_text='If a ranged weapon, any attack over normal range is made at disadvantage.')
    max_range = models.SmallIntegerField(null=False, blank=True, help_text='Maximum range a weapon can attack.')

    damage_dice_number = models.SmallIntegerField(help_text='Ex: Xd6 + 1.')
    damage_dice_size = models.SmallIntegerField(help_text='Ex: 1dX + 1.')
    damage_dice_bonus = models.SmallIntegerField(blank=True, null=True, help_text='Ex: 1d6 + X.')

    base_damage_type = models.ManyToManyField('rules.DamageType', related_name='weapon_base_damage_types', help_text='What kind of damage is done by the weapon.')
    properties = models.ManyToManyField('WeaponProperty', related_name='weapon_properties')


class Armor(Equipment):
    """Contains information regarding armor in the world."""

    ARMOR_TYPES = [
        ('Heavy', 'Heavy Armor'),
        ('Medium', 'Medium Armor'),
        ('Light', 'Light Armor'),
        ('Shield', 'Shield'),
    ]

    ARMOR_TIMES = [
        ('1 action', '1 action'),
        ('1 minute', '1 minute'),
        ('5 minutes', '5 minutes'),
        ('10 minutes', '10 minutes'),
    ]

    armor_type = models.CharField(max_length=16, choices=ARMOR_TYPES)

    base_armor_class = models.SmallIntegerField(null=True, blank=True)
    bonus_armor_class = models.SmallIntegerField(null=True, blank=True)
    dexterity_modifier = models.BooleanField(default=True,)
    dexterity_modifier_max = models.SmallIntegerField(null=True, blank=True,)

    don_time = models.CharField(max_length=16, choices=ARMOR_TIMES)
    doff_time = models.CharField(max_length=16, choices=ARMOR_TIMES)
    req_str = models.SmallIntegerField(null=True, blank=True,)
    stealth_disadvantage = models.BooleanField(default=False,)

    class Meta:
        verbose_name = 'Armor'
        verbose_name_plural = 'Armor'


class Tool(Equipment):
    """Subclass of items that are tools."""

    requires_proficiency = models.BooleanField(default=False)
    tool_type = models.CharField(max_length=128)


class EquipmentBonus(models.Model):
    """
    All possible bonuses a magic item can have.
    """
    # TODO: May have more to do on this one.

    name = models.CharField(max_length=100, unique=True, help_text='Name of the bonus.')
    description = models.CharField(max_length=1024)

    ability_score = models.CharField(max_length=16, null=True, blank=True,)
    ability_bonus = models.SmallIntegerField(null=True, blank=True,)

    damage_type = models.ForeignKey('rules.DamageType', related_name='equipment_bonus_damage_type', null=True, blank=True,)
    damage_bonus = models.SmallIntegerField(null=True, blank=True,)
    damage_dice_number = models.SmallIntegerField(null=True, blank=True,)
    damage_dice_size = models.SmallIntegerField(null=True, blank=True,)

    damage_resistance_type = models.ForeignKey('rules.DamageType', related_name='equipment_bonus_damage_resistance_type', blank=True, null=True,)

    advantage = models.BooleanField(default=False,)
    disadvantage = models.BooleanField(default=False,)
    check = models.CharField(max_length=128, null=True, blank=True,)

    skill = models.ForeignKey('rules.Skill', related_name='equipment_bonus_skill', null=True, blank=True,)
    skill_bonus = models.SmallIntegerField(null=True, blank=True,)

    spell = models.ForeignKey('spells.Spell', related_name='equipment_bonus_spell', null=True, blank=True,)
    spell_bonus = models.CharField(max_length=128, null=True, blank=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipment Bonus'
        verbose_name_plural = 'Equipment Bonuses'

class MountAndVehicle(Equipment):
    """
    All the mounts and vehicles in the game.
    """

    VEHICLE_TYPE = [
        ('Land', 'Land')
        ('Water', 'Water')
        ('Air', 'Air')
    ]

    speed = models.SmallIntegerField(null=True, blank=True,)
    carrying_capacity = models.SmallIntegerField(null=True, blank=True,)
    vehicle_type = models.CharField(max_length=16, choices=VEHICLE_TYPE)
