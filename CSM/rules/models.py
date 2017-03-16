"""
Models that describe the rules used by 5th Edition Dungeons and Dragons.

The goal is to make these loose enough to allow others to add new instances (such as classes),
but particular enough that the information will still be programmatically accessible for the actual CSM
"""

# TODO: limit_choices_to for limiting certain features. ??
# TODO: ADD SRD BOOLEAN FOR ALL MODELS!

# Django imports.
from django.db import models


DICE_SIZES = [
    (4, 4),
    (6, 6),
    (8, 8),
    (10, 10),
    (12, 12),
    (20, 20),
    (100, 100),
]

ABILITIES = [
        ('Strength', 'Strength'),
        ('Dexterity', 'Dexterity'),
        ('Constitution', 'Constitution'),
        ('Intelligence', 'Intelligence'),
        ('Wisdom', 'Wisdom'),
        ('Charisma', 'Charisma'),
    ]

ARMOR_TYPES = [
        ('Heavy', 'Heavy Armor'),
        ('Medium', 'Medium Armor'),
        ('Light', 'Light Armor'),
        ('Shield', 'Shield'),
    ]

STATS = [
        ('Speed', 'Speed'),
        ('AC', 'Armor Class'),
        ('Initiative', 'Initiative'),
        ('Age', 'Age'),
        ('Size', 'Size'),
        ('Rest', 'Long Rest Duration'),
        ('Sight', 'Sight'),
        ('Sight - Darkvision', 'Sight - Darkvision'),
        ('HP', 'Hit Points'),
    ]

ACTIONS = [
        ('Attack', 'Attack'),
        ('Cast', 'Cast a Spell'),
        ('Dash', 'Dash'),
        ('Disengage', 'Disengage'),
        ('Dodge', 'Dodge'),
        ('Help', 'Help'),
        ('Hide', 'Hide'),
        ('Ready', 'Ready'),
        ('Search', 'Search'),
        ('Use', 'Use an Object'),
        ('Action', 'Action'),
        ('Bonus', 'Bonus Action'),
        ('Reaction', 'Reaction'),
        ('Move', 'Move'),
        ('None', 'None'),
    ]


class Subrace(models.Model):
    """Subraces for races."""

    # Basic Information:
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)

    # Ability Score Bonuses:
    ability_score_1 = models.CharField(max_length=16, choices=ABILITIES)
    ability_score_1_bonus = models.SmallIntegerField(blank=True, null=True,)

    ability_score_2 = models.CharField(max_length=16, choices=ABILITIES, blank=True, null=True)
    ability_score_2_bonus = models.SmallIntegerField(blank=True, null=True,)

    # Features:
    features = models.ManyToManyField('Feature', related_name='subrace_features')

    # Additional Starting Equipment:
    subrace_tool_starts = models.ManyToManyField('equipment.Tool', related_name='subrace_tool_starts', blank=True,)
    subrace_weapon_starts = models.ManyToManyField('equipment.Weapon', related_name='subrace_weapon_starts', blank=True,)
    subrace_armor_starts = models.ManyToManyField('equipment.Armor', related_name='subrace_armor_starts', blank=True,)
    subrace_item_starts = models.ManyToManyField('equipment.Item', related_name='subrace_item_starts', blank=True,)

    def __str__(self):
        return self.name


class Race(models.Model):
    """Information about races in D&D"""

    SIZES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Huge', 'Huge'),
        ('Gargantuan', 'Gargantuan'),
    ]

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=10000)

    # Ability Bonuses:
    ability_score_1 = models.CharField(max_length=16)
    ability_score_1_bonus = models.SmallIntegerField(blank=True, null=True,)

    ability_score_2 = models.CharField(max_length=16, blank=True, null=True)
    ability_score_2_bonus = models.SmallIntegerField(blank=True, null=True,)

    # Age and Alignment:
    age_adult = models.SmallIntegerField()
    age_mortality = models.SmallIntegerField()
    typical_alignment = models.ForeignKey('Alignment', related_name='race_alignment')

    # Basic information:
    size = models.CharField(max_length=16, choices=SIZES)
    typical_height_min = models.SmallIntegerField()
    typical_height_max = models.SmallIntegerField()
    typical_weight_min = models.SmallIntegerField()
    typical_weight_max = models.SmallIntegerField()
    speed = models.SmallIntegerField()
    speed_special = models.CharField(max_length=128, blank=True, null=True,)

    features = models.ManyToManyField('Feature', related_name='race_features')

    # Starting Equipment:
    race_tool_starts = models.ManyToManyField('equipment.Tool', related_name='race_tool_starts', blank=True,)
    race_weapon_starts = models.ManyToManyField('equipment.Weapon', related_name='race_weapon_starts', blank=True,)
    race_armor_starts = models.ManyToManyField('equipment.Armor', related_name='race_armor_starts', blank=True,)
    race_item_starts = models.ManyToManyField('equipment.Item', related_name='race_item_starts', blank=True,)

    subraces = models.ManyToManyField('Subrace', related_name='race_subraces', blank=True,)

    def __str__(self):
        return self.name


class PrestigeClass(models.Model):
    """
    Information about prestige classes.
    """

    # Basic Information:
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=10000)

    # number_of_skills = models.SmallIntegerField(blank=True, null=True,)

    # Features
    features = models.ManyToManyField('Feature', related_name='prestige_class_features')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Prestige Class"
        verbose_name_plural = "Prestige Classes"


class Class(models.Model):
    """Information about classes."""

    # Basic Information:
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=10000)

    hit_die_size = models.SmallIntegerField(choices=DICE_SIZES)

    # Abilities and Saving Throws:
    primary_ability_1 = models.CharField(max_length=16, choices=ABILITIES)
    primary_ability_2 = models.CharField(max_length=16, choices=ABILITIES, blank=True, null=True,)

    saving_throw_1 = models.CharField(max_length=16, choices=ABILITIES)
    saving_throw_2 = models.CharField(max_length=16, choices=ABILITIES, blank=True, null=True,)

    # Starting Wealth/Equipment
    starting_gold = models.SmallIntegerField(blank=True, null=True,)
    starting_weapons = models.ManyToManyField('equipment.Weapon', related_name='class_weapon_starts', blank=True,)
    starting_armor = models.ManyToManyField('equipment.Armor', related_name='class_armor_starts', blank=True,)
    starting_items = models.ManyToManyField('equipment.Item', related_name='classes_item_start', blank=True,)
    starting_tools = models.ManyToManyField('equipment.Tool', related_name='classes_tool_start', blank=True,)

    # Features
    features = models.ManyToManyField('Feature', related_name='class_features')
    prestige_classes = models.ManyToManyField('PrestigeClass', related_name='class_prestige_classes', blank=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"


class Feature(models.Model):
    """
    Information about race, class, subrace, subclass, and background features.

    This is one of the heaviest lifters in the database because it will describe all possible interactions a player
    can take, excepting spells and items.
    """

    # Basic Information:
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=10000)

    # Feature Modifiers
    is_proficiency = models.BooleanField(default=False,)
    is_choice = models.BooleanField(default=False,)
    changes_at_level = models.BooleanField(default=False,)
    grants_advantage = models.BooleanField(default=False,)

    # Feature Actions
    action_type = models.CharField(max_length=64, choices=ACTIONS, blank=True, null=True)
    action_constraint_start = models.CharField(max_length=128, blank=True, null=True)
    action_constraint_end = models.CharField(max_length=128, blank=True, null=True)
    action_duration = models.CharField(max_length=128, blank=True, null=True)
    action_distance = models.CharField(max_length=128, blank=True, null=True)
    action_use_stat = models.CharField(max_length=128, blank=True, null=True) # TODO: NOT SURE ABOUT THIS ONE....
    action_uses_per_day = models.CharField(max_length=128, blank=True, null=True)

    # Ability Score Modification
    ability_to_change = models.CharField(max_length=32, choices=ABILITIES, blank=True, null=True,)
    ability_change_amount = models.SmallIntegerField(blank=True, null=True,)
    stat_to_change = models.CharField(max_length=32, choices=STATS, blank=True, null=True,)
    stat_change_amount = models.SmallIntegerField(blank=True, null=True,)

    # Proficiencies
    weapon_prof = models.ManyToManyField('equipment.Weapon', related_name='feature_weapon_profs', blank=True,)
    armor_prof = models.CharField(max_length=32, choices=ARMOR_TYPES, blank=True, null=True,)
    tool_prof = models.ManyToManyField('equipment.Tool', related_name='feature_tool_profs', blank=True,)
    skill_prof = models.ManyToManyField('Skill', related_name='feature_skill_profs', blank=True,)
    languages_known = models.ManyToManyField('Language', related_name='feature_languages', blank=True,)

    # Feature Multiple Spells:
    spell_choice = models.ManyToManyField('spells.Spell', related_name='feature_spell_choices', blank=True,)
    spell_choice_number = models.SmallIntegerField(blank=True, null=True,)
    spell_choice_level = models.SmallIntegerField(blank=True, null=True,)
    spell_choices_class_list = models.CharField(max_length=512, blank=True, null=True,)

    # Feature Single Spell:
    spell_known = models.ForeignKey('spells.Spell', related_name='feature_spell_known', blank=True, null=True,)
    spell_known_constraint = models.CharField(max_length=512, blank=True, null=True,)

    # Feature Damage:
    damage_type = models.ForeignKey('DamageType', related_name='feature_damage_types', blank=True, null=True,)
    damage_dice_number = models.SmallIntegerField(blank=True, null=True,)
    damage_dice_size = models.SmallIntegerField(choices=DICE_SIZES, blank=True, null=True,)
    damage_dice_bonus = models.SmallIntegerField(blank=True, null=True,)

    # Feature Resistances:
    damage_resistance_type = models.ManyToManyField('DamageType', related_name='feature_damage_resistance_types', blank=True,)
    spell_resistance = models.BooleanField(default=False,)
    condition_resistance = models.ManyToManyField('Condition', related_name='feature_conditions', blank=True,)

    # Feature Prerequisites
    prereq_ability = models.CharField(max_length=16, choices=ABILITIES, blank=True, null=True,)
    prereq_ability_amount = models.SmallIntegerField(blank=True, null=True,)
    prereq_proficiency = models.ManyToManyField('Feature', related_name='feature_prereq_proficiency', blank=True,)
    prereq_character_level = models.SmallIntegerField(blank=True, null=True,)
    prereq_class = models.ForeignKey('Class', related_name='feature_prereq_class', blank=True, null=True,)
    prereq_class_level = models.SmallIntegerField(blank=True, null=True,)
    prereq_prestige_class = models.ForeignKey('PrestigeClass', related_name='feature_prereq_prestige_class', blank=True, null=True,)
    prereq_race = models.ForeignKey('Race', related_name='feature_prereq_race', blank=True, null=True,)
    prereq_subrace = models.ForeignKey('Subrace', related_name='feature_prereq_subrace', blank=True, null=True,)

    def __str__(self):
        return self.name


class Background(models.Model):
    """
    The model for character backgrounds.
    """

    #  Basic Information:
    name = models.CharField(max_length=128,)
    description = models.CharField(max_length=10000,)

    languages = models.ManyToManyField('Language', related_name='background_languages', blank=True,)
    features = models.ManyToManyField('Feature', related_name='background_features', blank=True,)

    # Starting Wealth/Equipment
    gold_start = models.SmallIntegerField()
    tool_starts = models.ManyToManyField('equipment.Tool', related_name='background_tool_starts', blank=True,)
    item_starts = models.ManyToManyField('equipment.Item', related_name='background_item_starts', blank=True,)
    weapon_starts = models.ManyToManyField('equipment.Weapon', related_name='background_weapon_starts', blank=True,)
    armor_starts = models.ManyToManyField('equipment.Armor', related_name='background_armor_starts', blank=True,)
    specials = models.CharField(max_length=512, null=True, blank=True)

    # Suggested Flair
    suggested_personality_traits = models.ManyToManyField('PersonalityTrait', related_name='background_personality_traits', blank=True,)
    suggested_ideals = models.ManyToManyField('Ideal', related_name='background_ideals', blank=True,)
    suggested_bonds = models.ManyToManyField('Bond', related_name='background_bonds', blank=True,)
    suggested_flaws = models.ManyToManyField('Flaw', related_name='background_flaws', blank=True,)

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Model for describing skills."""

    name = models.CharField(max_length=128,)
    associated_ability = models.CharField(max_length=16, choices=ABILITIES,)
    description = models.CharField(max_length=10000,)
    example_tasks = models.CharField(max_length=512, blank=True, null=True,)

    def __str__(self):
        return self.name


class Language(models.Model):
    """Model for describing languages."""

    name = models.CharField(max_length=128,)
    description = models.CharField(max_length=10000,)
    typical_speakers = models.CharField(max_length=512,)
    script = models.CharField(max_length=512, blank=True, null=True,)

    def __str__(self):
        return self.name


class DamageType(models.Model):
    """Model for types of damage."""

    name = models.CharField(max_length=128,)
    description = models.CharField(max_length=512,)

    def __str__(self):
        return self.name


class Condition(models.Model):
    """Model for different conditions."""

    # TODO: Make a better model for programmatic access.

    name = models.CharField(max_length=128,)
    description = models.CharField(max_length=1024,)

    def __str__(self):
        return self.name


class Alignment(models.Model):
    """Model for different Alignments."""

    name = models.CharField(max_length=64,)
    description = models.CharField(max_length=1024,)
    # TODO: Add examples column.
    def __str__(self):
        return self.name


class PersonalityTrait(models.Model):
    """Model for basic suggested personality traits."""

    name = models.CharField(max_length=128, blank=True, null=True,)
    description = models.CharField(max_length=1024,)

    def __str__(self):
        return self.name


class Ideal(models.Model):
    """Model for basic suggested ideals."""

    name = models.CharField(max_length=128, blank=True, null=True,)
    description = models.CharField(max_length=1024,)

    def __str__(self):
        return self.name


class Bond(models.Model):
    """Model for basic suggested bonds."""

    name = models.CharField(max_length=128, blank=True, null=True,)
    description = models.CharField(max_length=1024,)

    def __str__(self):
        return self.name


class Flaw(models.Model):
    """Model for basic suggested flaws."""

    name = models.CharField(max_length=128, blank=True, null=True,)
    description = models.CharField(max_length=1024,)

    def __str__(self):
        return self.name
