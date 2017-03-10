from django.db import models

# Create your models here.

class Spell(models.Model):
    """Gives basic interface of spells in 5th Edition Dungeons and Dragons"""

    SPELL_SAVES = (
        ('STR', 'Strength'),
        ('DEX', 'Dexterity'),
        ('CON', 'Constitution'),
        ('INT', 'Intelligence'),
        ('WIS', 'Wisdom'),
        ('CHA', 'Charisma'),
        ('NON', 'None'),
    )

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

    SPELL_SCHOOL = (
        ('Abjuration', 'Abjuration'),
        ('Conjuration', 'Conjuration'),
        ('Divination', 'Divination'),
        ('Enchantment', 'Enchantment'),
        ('Evocation', 'Evocation'),
        ('Illusion', 'Illusion'),
        ('Necromancy', 'Necromancy'),
        ('Transmutation', 'Transmutation'),
    )

    CAST_TIME = (
        ('1 Action', '1 Action'),
        ('1 Bonus Action', '1 Bonus Action'),
        ('1 Reaction', '1 Reaction'),
        ('1 Minute', '1 Minute'),
        ('10 Minutes', '10 Minutes'),
        ('1 Hour', '1 Hour'),
        ('8 Hours', '8 Hours'),
        ('12 Hours', '12 Hours'),
        ('24 Hours', '24 Hours'),
        ('1 Action or 8 Hours', '1 Action or 8 Hours')
    )

    SPELL_LEVELS = (
        ('Cantrip', 'Cantrip'),
        ('1st-level', '1st-level'),
        ('2nd-level', '2nd-level'),
        ('3rd-level', '3rd-level'),
        ('4th-level', '4th-level'),
        ('5th-level', '5th-level'),
        ('6th-level', '6th-level'),
        ('7th-level', '7th-level'),
        ('8th-level', '8th-level'),
        ('9th-level', '9th-level')
    )

    name = models.CharField(max_length=128, help_text='Name of the spell.')
    school = models.CharField(max_length=24, choices=SPELL_SCHOOL, help_text='Magical school for the spell.')
    level = models.CharField(max_length=12, choices=SPELL_LEVELS, help_text='Level of the spell.')
    available_to = models.CharField(max_length=256, help_text='Classes that are allowed to cast the spell.')

    cast_time = models.CharField(max_length=24, choices=CAST_TIME, help_text='Cast time for a spell.')
    distance = models.CharField(max_length=128, help_text='Maximum distance the spell can be cast up to.')
    duration = models.CharField(max_length=128, help_text='Duration of the spell.')
    concentration = models.BooleanField(default=False, help_text='Whether a spell requires concentration.')
    ritual = models.BooleanField(default=False, help_text='Whether a spell is castable as a ritual.')

    material = models.BooleanField(default=False, help_text='Does the spell require material components?')
    somatic = models.BooleanField(default=False, help_text='Does the spell require somatic components?')
    verbal = models.BooleanField(default=False, help_text='Does the spell require verbal components?')
    specific_materials = models.CharField(blank=True, null=True, max_length=256, help_text='If a spell requires material components, which specific materials does the spell require?')

    description = models.TextField(help_text='Full description of the spell.')
    save_type = models.CharField(blank=True, null=True, max_length=3, choices=SPELL_SAVES, help_text='Which save ability is used if any.')
    damage_dice_number = models.SmallIntegerField(blank=True, null=True, help_text='Ex: Xd6 + 1.')
    damage_dice_size = models.SmallIntegerField(blank=True, null=True, help_text='Ex: 1dX + 1.')
    damage_dice_bonus = models.SmallIntegerField(blank=True, null=True, help_text='Ex: 1d6 + X.')
    damage_type = models.CharField(blank=True, null=True, max_length=2, choices=DAMAGE_TYPE, help_text='What kind of damage is done by the spell.')
    targets = models.SmallIntegerField(blank=True, null=True, help_text='Number of possible targets (usually not used).')
    higher_level = models.TextField(blank=True, null=True, help_text='Extra effects to use if cast at a higher level.')
    special = models.CharField(max_length=256, blank=True, null=True, help_text='General special information for a spell.')

    phb_page = models.SmallIntegerField(blank=True, null=True, help_text="Between pages 211 and 289 in the Player's Handbook.")

    @property
    def raw_materials(self):
        raw_string = ''
        if self.verbal:
            raw_string += 'V '

        if self.somatic:
            raw_string += 'S '

        if self.material:
            raw_string += 'M '
            raw_string += self.specific_materials

        return raw_string

    def __str__(self):
        return self.name


class SpellBook(models.Model):
    """
    Model that stores all spells available to a character.
    """

