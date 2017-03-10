# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the spell.', max_length=128)),
                ('school', models.CharField(choices=[('Abjuration', 'Abjuration'), ('Conjuration', 'Conjuration'), ('Divination', 'Divination'), ('Enchantment', 'Enchantment'), ('Evocation', 'Evocation'), ('Illusion', 'Illusion'), ('Necromancy', 'Necromancy'), ('Transmutation', 'Transmutation')], help_text='Magical school for the spell.', max_length=24)),
                ('level', models.CharField(choices=[('Cantrip', 'Cantrip'), ('1st-level', '1st-level'), ('2nd-level', '2nd-level'), ('3rd-level', '3rd-level'), ('4th-level', '4th-level'), ('5th-level', '5th-level'), ('6th-level', '6th-level'), ('7th-level', '7th-level'), ('8th-level', '8th-level'), ('9th-level', '9th-level')], help_text='Level of the spell.', max_length=12)),
                ('available_to', models.CharField(help_text='Classes that are allowed to cast the spell.', max_length=256)),
                ('cast_time', models.CharField(choices=[('1 Action', '1 Action'), ('1 Bonus Action', '1 Bonus Action'), ('1 Reaction', '1 Reaction'), ('1 Minute', '1 Minute'), ('10 Minutes', '10 Minutes'), ('1 Hour', '1 Hour'), ('8 Hours', '8 Hours'), ('12 Hours', '12 Hours'), ('24 Hours', '24 Hours'), ('1 Action or 8 Hours', '1 Action or 8 Hours')], help_text='Cast time for a spell.', max_length=24)),
                ('distance', models.CharField(help_text='Maximum distance the spell can be cast up to.', max_length=128)),
                ('duration', models.CharField(help_text='Duration of the spell.', max_length=128)),
                ('concentration', models.BooleanField(default=False, help_text='Whether a spell requires concentration.')),
                ('ritual', models.BooleanField(default=False, help_text='Whether a spell is castable as a ritual.')),
                ('material', models.BooleanField(default=False, help_text='Does the spell require material components?')),
                ('somatic', models.BooleanField(default=False, help_text='Does the spell require somatic components?')),
                ('verbal', models.BooleanField(default=False, help_text='Does the spell require verbal components?')),
                ('specific_materials', models.CharField(blank=True, help_text='If a spell requires material components, which specific materials does the spell require?', max_length=256, null=True)),
                ('description', models.TextField(help_text='Full description of the spell.')),
                ('save_type', models.CharField(blank=True, choices=[('STR', 'Strength'), ('DEX', 'Dexterity'), ('CON', 'Constitution'), ('INT', 'Intelligence'), ('WIS', 'Wisdom'), ('CHA', 'Charisma'), ('NON', 'None')], help_text='Which save ability is used if any.', max_length=3, null=True)),
                ('damage_dice_number', models.SmallIntegerField(blank=True, help_text='Ex: Xd6 + 1.', null=True)),
                ('damage_dice_size', models.SmallIntegerField(blank=True, help_text='Ex: 1dX + 1.', null=True)),
                ('damage_dice_bonus', models.SmallIntegerField(blank=True, help_text='Ex: 1d6 + X.', null=True)),
                ('damage_type', models.CharField(blank=True, choices=[('AC', 'Acid'), ('BL', 'Bludgeoning'), ('CO', 'Cold'), ('FI', 'Fire'), ('FO', 'Force'), ('LI', 'Lightning'), ('NE', 'Necrotic'), ('PI', 'Piercing'), ('PO', 'Poison'), ('PS', 'Psychic'), ('RA', 'Radiant'), ('SL', 'Slashing'), ('TH', 'Thunder')], help_text='What kind of damage is done by the spell.', max_length=2, null=True)),
                ('targets', models.SmallIntegerField(blank=True, help_text='Number of possible targets (usually not used).', null=True)),
                ('higher_level', models.TextField(blank=True, help_text='Extra effects to use if cast at a higher level.', null=True)),
                ('special', models.CharField(blank=True, help_text='General special information for a spell.', max_length=256, null=True)),
                ('phb_page', models.SmallIntegerField(blank=True, help_text="Between pages 211 and 289 in the Player's Handbook.", null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpellBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
