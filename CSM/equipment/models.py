from django.db import models

# Create your models here.

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

    DAMAGE_TYPE = (
        ('AC', 'Acid'),
        ('BL', 'Bludgeoning'),
        ('CO', 'Cold'),
        ('FI', 'Fire'),
        ('FO', 'Force'),
        ('LI', 'Lightning'),
        ('NE', 'Necrotic'),
        ('PI', 'Piercing'),
        ('PO', 'Poison'),
        ('PS', 'Psychic'),
        ('RA', 'Radiant'),
        ('SL', 'Slashing'),
        ('TH', 'Thunder'),
    )

    name = models.CharField(max_length=100, unique=True, help_text='Name of the weapon.')
    simple_or_martial = models.BooleanField(default=False, help_text='False = Simple Weapon, True = Martial Weapon.')
    melee_or_ranged = models.BooleanField(default=False, help_text='False = Melee Weapon, True = Ranged Weapon.')
    normal_range = models.SmallIntegerField(null=True, blank=True, help_text='If a ranged weapon, any attack over normal range is made at disadvantage.')
    max_range = models.SmallIntegerField(null=False, blank=True, help_text='Maximum range a weapon can attack.')

    cost_copper = models.SmallIntegerField(null=True, blank=True, help_text='Cost in copper pieces.')
    cost_silver = models.SmallIntegerField(null=True, blank=True, help_text='Cost in silver pieces.')
    cost_gold = models.SmallIntegerField(null=True, blank=True, help_text='Cost in gold pieces.')
    cost_platinum = models.SmallIntegerField(null=True, blank=True, help_text='Cost in platinum pieces.')

    damage_dice_number = models.SmallIntegerField(help_text='Ex: Xd6 + 1.')
    damage_dice_size = models.SmallIntegerField(help_text='Ex: 1dX + 1.')
    damage_dice_bonus = models.SmallIntegerField(blank=True, null=True, help_text='Ex: 1d6 + X.')

    damage_type = models.CharField(max_length=2, choices=DAMAGE_TYPE, help_text='What kind of damage is done by the weapon.')
    weight = models.SmallIntegerField(help_text='Carrying weight of the weapon.')
    properties = models.ManyToManyField(WeaponProperty, related_name='weapons')
    description = models.TextField(help_text='Full description of the weapon.')
    special = models.CharField(max_length=100, blank=True, null=True, help_text='General field for additional rules.')

    def __str__(self):
        return self.name


class Armor(models.Model):
    """Contains information regarding armor in the world."""

    name = models.CharField(max_length=100, unique=True, help_text='Name of the armor.')
    # armor_type
    # cost
    # armor_class
    # req_str
    # stealth
    # weight
    # description
    # special

    def __str__(self):
        return self.name

class Item(models.Model):
    """Contains information on other items in the world."""

    name = models.CharField(max_length=100, unique=True, help_text='Name of the item.')
    # item_type
    # uses
    # space
    # cost
    # weight
    # description
    # special

    def __str__(self):
        return self.name


class EquipmentBonus(models.Model):
    """All possible bonuses a magic item can have."""

    name = models.CharField(max_length=100, unique=True, help_text='Name of the bonus.')
    # description
    # ability_score
    # ability_bonus
    # damage_type
    # damage_bonus
    # advantage
    # skill
    # skill_bonus
    # spell
    # spell_bonus

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipment Bonus'
        verbose_name_plural = 'Equipment Bonuses'
