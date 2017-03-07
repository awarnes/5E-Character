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
        ('AB', 'Abjuration'),
        ('CO', 'Conjuration'),
        ('DI', 'Divination'),
        ('EN', 'Enchantment'),
        ('EV', 'Evocation'),
        ('IL', 'Illusion'),
        ('NE', 'Necromancy'),
        ('TR', 'Transmutation'),
    )

    CAST_TIME = (
        ('AC', '1 Action'),
        ('BA', '1 Bonus Action'),
        ('RE', '1 Reaction'),
        ('1M', '1 Minute'),
        ('10', '10 Minutes'),
        ('1H', '1 Hour'),
        ('8H', '8 Hours'),
        ('12', '12 Hours'),
        ('24', '24 Hours'),
    )

    SPELL_LEVELS = (
        (0, 'Cantrip'),
        (1, '1st-level'),
        (2, '2nd-level'),
        (3, '3rd-level'),
        (4, '4th-level'),
        (5, '5th-level'),
        (6, '6th-level'),
        (7, '7th-level'),
        (8, '8th-level'),
        (9, '9th-level')
    )

    SPELL_COMPONENTS = (
        ('V', 'Verbal'),
        ('S', 'Somatic'),
        ('M', 'Material')
    )

    name = models.CharField(max_length=100, unique=True, help_text='Name of the spell.')
    school = models.CharField(max_length=2, choices=SPELL_SCHOOL, help_text='Magical school for the spell.')
    level = models.CharField(max_length=1, choices=SPELL_LEVELS, help_text='Level of the spell.')

    cast_time = models.CharField(max_length=2, choices=CAST_TIME, help_text='Cast time for a spell.')
    distance = models.SmallIntegerField(help_text='Distance the spell can be cast up to in feet; 0 = self.')
    duration = models.SmallIntegerField(help_text='Duration of the spell in minutes; 0 = instant, -1 = infinite (until dispelled).')
    concentration = models.BooleanField(default=False, help_text='Whether a spell requires concentration.')
    components = models.CharField(max_length=1, choices=SPELL_COMPONENTS, help_text='Which of the three types of components are required for a spell.')
    materials = models.CharField(max_length=256, help_text='Which specific materials does the spell require.')

    description = models.TextField(help_text='Full description of the spell.')
    save_type = models.CharField(max_length=3, choices=SPELL_SAVES, help_text='Which save ability is used if any.')
    damage_dice_number = models.SmallIntegerField(help_text='Ex: Xd6 + 1.')
    damage_dice_size = models.SmallIntegerField(help_text='Ex: 1dX + 1.')
    damage_dice_bonus = models.SmallIntegerField(blank=True, null=True, help_text='Ex: 1d6 + X.')
    damage_type = models.CharField(max_length=2, choices=DAMAGE_TYPE, help_text='What kind of damage is done by the spell.')
    targets = models.SmallIntegerField(blank=True, null=True, help_text='Number of possible targets (usually not used).')
    higher_level_damage = models.SmallIntegerField(blank=True, null=True, help_text='Extra dice to use if cast at a higher level.')
    special = models.CharField(max_length=100, blank=True, null=True, help_text='General special information for a spell.')

    phb_page = models.SmallIntegerField(help_text="Between pages 211 and 289 in the Player's Handbook.")

    def __str__(self):
        return self.name