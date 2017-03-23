"""
All the views that a user will see on the site.
"""
import pdb

# Python Imports:
import re


# Django Imports:
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView

from django.db.models import Q
from django.contrib import messages

# Module and Form Imports:
from .forms import SearchDatabase
from .forms import AbilityScoresChoice, CCRace, CCClass, CCPersonality, CCBackground, CCEquipment, NCResolve

# Model Imports:
from rules.models import (Alignment, Class, PrestigeClass, Race, Subrace, DamageType, Feature, Skill, Background,
                          Language, Condition, )
from spells.models import Spell
from character.models import Character, ClassLevel
from equipment.models import (Weapon, Armor, Tool, Item, MountAndVehicle)
from accounts.models import Member


def landing(request):

    context = dict()

    # messages.info(request, "Hello there! Welcome!")

    return render(request, 'landing.html', context)


def about_us(request):
    """
    Basic contact form for web page.
    """

    context = {'title': 'About Us!'}

    return render(request, 'company/about_us.html', context)


def report_issue(request):
    """
    Basic contact form for web page.
    """

    context = {'title': 'Report an Issue!'}

    return render(request, 'company/report_issue.html', context)


def search_home(request):
    """Shows the home search screen and allows the user to search for all the things."""

    if request.method == 'GET':
        query = ''
        results = dict()
        total = 0

    elif request.method == 'POST':
        models = (Spell, Weapon, Armor, Item, Tool, Feature, Class, Race, PrestigeClass, Subrace,
                  Skill, Alignment, DamageType, MountAndVehicle, Background, Language, Condition)
        results = dict()
        query = request.POST.get('query')
        total = 0

        for model in models:
            found = model.objects.filter(name__icontains=query)
            model_name = ' '.join(re.findall(r'[A-Z][a-z]+', str(model)))

            if found and model_name[-1] == 's':
                model_name += 'es'
                results[model_name] = list()
                for item in found:
                    results[model_name].append(item)
                    total += 1

            elif found and model_name[-1] != 's':
                model_name += 's'
                results[model_name] = list()
                for item in found:
                    results[model_name].append(item)
                    total += 1

    context = {'query': query, 'results': results, 'total': total}

    return render(request, 'database_view/search_home.html', context)


# Rule Detail Views:
def spell_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    spell = get_object_or_404(Spell, slug=slug)

    classes = list()
    for klass in spell.available_to.split(', '):
        if klass != '':
            classes.append(klass)

    context = {'result': spell, 'classes': classes, 'rit': spell.ritual, 'con': spell.concentration}

    return render(request, 'database_view/detail_pages/spell_details.html', context)


def subrace_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    subrace = get_object_or_404(Subrace, slug=slug)

    context = {'result': subrace, 'features': subrace.features.all(), 'parent': subrace.race_subraces.get()}

    return render(request, 'database_view/detail_pages/subrace_details.html', context)


def race_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    race = get_object_or_404(Race, slug=slug)

    context = {'result': race, 'features': race.features.all(), 'subraces': race.subraces.all()}

    return render(request, 'database_view/detail_pages/race_details.html', context)


def prestige_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    prestige = get_object_or_404(PrestigeClass, slug=slug)

    context = {'result': prestige, 'features': prestige.features.all(), 'parent': prestige.class_prestige_classes.get()}

    return render(request, 'database_view/detail_pages/prestige_details.html', context)


def class_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    klass = get_object_or_404(Class, slug=slug)

    pa2 = False
    if klass.primary_ability_2 != 'None':
        pa2 = True;

    context = {'result': klass, 'prestiges': klass.prestige_classes.all(), 'pa2': pa2, 'features': klass.features.all()}

    return render(request, 'database_view/detail_pages/class_details.html', context)


def feature_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    feature = get_object_or_404(Feature, slug=slug)

    parent = False
    search_type = None

    try:
        parent = feature.class_features.all()
        search_type = 'classes'
    except ObjectDoesNotExist:
        pass
    try:
        parent = feature.prestige_class_features.all()
        search_type = 'prestige_classes'
    except ObjectDoesNotExist:
        pass
    try:
        parent = feature.race_features.all()
        search_type = 'races'
    except ObjectDoesNotExist:
        pass
    try:
        parent = feature.subrace_features.all()
        search_type = 'subraces'
    except ObjectDoesNotExist:
        pass
    try:
        parent = feature.background_features.all()
        search_type = 'backgrounds'
    except ObjectDoesNotExist:
        pass

    context = {'result': feature, 'parent': parent, 'type': search_type}

    return render(request, 'database_view/detail_pages/feature_details.html', context)


def background_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    background = get_object_or_404(Background, slug=slug)

    context = {'result': background, 'features': background.features.all()}

    return render(request, 'database_view/detail_pages/background_details.html', context)


def skill_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    skill = get_object_or_404(Skill, slug=slug)

    context = {'result': skill}

    return render(request, 'database_view/detail_pages/skill_details.html', context)


def language_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    language = get_object_or_404(Language, slug=slug)

    context = {'result': language}

    return render(request, 'database_view/detail_pages/language_details.html', context)


def condition_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    condition = get_object_or_404(Condition, slug=slug)

    context = {'result': condition}

    return render(request, 'database_view/detail_pages/condition_details.html', context)


# Equipment Detail Views:
def item_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    item = get_object_or_404(Item, slug=slug)

    context = {'result': item}

    return render(request, 'database_view/detail_pages/item_details.html', context)


def weapon_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    weapon = get_object_or_404(Weapon, slug=slug)

    ranged = False
    if weapon.melee_or_ranged == 'Ranged':
        ranged = True

    dmg_type = weapon.base_damage_type.get()

    context = {'result': weapon, 'ranged': ranged, 'properties': weapon.properties.all(), 'dmg_type': dmg_type.name}

    return render(request, 'database_view/detail_pages/weapon_details.html', context)


def armor_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    armor = get_object_or_404(Armor, slug=slug)

    maximum = False

    if armor.dexterity_modifier_max > 0:
        maximum = armor.dexterity_modifier_max

    minute = False
    if armor.don_time != '1 action':
        minute = True

    context = {'result': armor, 'max': maximum, 'minute': minute}

    return render(request, 'database_view/detail_pages/armor_details.html', context)


def tool_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    tool = get_object_or_404(Tool, slug=slug)

    context = {'result': tool}

    return render(request, 'database_view/detail_pages/tool_details.html', context)


def mount_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    mount = get_object_or_404(MountAndVehicle, slug=slug)

    speed = 'feet'
    if mount.vehicle_type == 'Water':
        speed = 'mph'

    context = {'result': mount, 'speed': speed}

    return render(request, 'database_view/detail_pages/mount_details.html', context)


# Character Creation Screens (CC):
@method_decorator(login_required, name='dispatch')
class CharacterCreationName(CreateView):
    """First view in the character creation flow."""

    model = Character
    fields = ['char_name',]
    success_url = reverse_lazy('nc_race')
    template_name = 'characters/char_creation_name.html'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super(CharacterCreationName, self).form_valid(form)


@login_required()
def nc_race(request):
    """Choose a race and subclass if available."""

    if request.method == "GET":
        character = request.user.characters.latest('accessed')
        request.session['character'] = character.pk
        form = CCRace()

        context = {'race_form': form, 'character': character}

        return render(request, 'characters/nc_race.html', context)

    elif request.method == "POST":
        character = Character.objects.get(pk=request.session['character'])
        form = CCRace(data=request.POST)

        context = {'race_form': form, 'character': character}

        if form.is_valid():

            character.char_race = form.cleaned_data['race']
            character.char_subrace = form.cleaned_data['subrace']
            character.save()

            request.session['character'] = character.pk

            return redirect('nc_class')

        return render(request, 'characters/nc_race.html', context)


@login_required()
def nc_class(request):
    """Choose a class for new character."""

    if request.method == "GET":
        character = Character.objects.get(pk=request.session['character'])
        form = CCClass()

        context = {'character': character, 'class_form': form}

        return render(request, 'characters/nc_class.html', context)

    elif request.method == "POST":
        character = Character.objects.get(pk=request.session['character'])
        form = CCClass(data=request.POST)

        context = {'class_form': form, 'character': character}

        if form.is_valid():

            ClassLevel.objects.create(
                character=character,
                char_class=form.cleaned_data['klass'],
                class_level=1
            )

            if form.cleaned_data['klass'] == Class.objects.get(name='Cleric'):
                character.char_prestige = form.cleaned_data['cleric_prestige']

            elif form.cleaned_data['klass'] == Class.objects.get(name='Sorcerer'):
                character.char_prestige = form.cleaned_data['sorcerer_prestige']

            elif form.cleaned_data['klass'] == Class.objects.get(name='Warlock'):
                character.char_prestige = form.cleaned_data['warlock_prestige']

            else:
                character.char_prestige = PrestigeClass.objects.get(name='None')

            character.max_health = form.cleaned_data['hp']
            character.current_health = form.cleaned_data['hp']

            character.save()

            request.session['character'] = character.pk

            return redirect('nc_ability_scores')

        return render(request, 'characters/nc_class.html', context)


@login_required()
def nc_ability_scores(request):
    """
    Help with character creation?
    """

    if request.method == "GET":
        choice_form = AbilityScoresChoice()
        roll_form = AbilityScoresChoice()
        buy_form = AbilityScoresChoice()
        class_level = ClassLevel.objects.filter(character__pk=request.session['character'])
        character = Character.objects.get(pk=request.session['character'])

        context = {'character': character, 'class_level': class_level, 'choice_form': choice_form, 'roll_form': roll_form, 'buy_form': buy_form}

        return render(request, 'characters/nc_ability_scores.html', context)

    elif request.method == "POST":
        form = AbilityScoresChoice(data=request.POST)
        class_level = ClassLevel.objects.filter(character__pk=request.session['character'])
        character = Character.objects.get(pk=request.session['character'])

        context = {'character': character, 'class_level': class_level, 'form': form}


        if form.is_valid():
            character = Character.objects.get(pk=request.session['character'])
            character.STR_score = form.cleaned_data['Strength']
            character.DEX_score = form.cleaned_data['Dexterity']
            character.CON_score = form.cleaned_data['Constitution']
            character.INT_score = form.cleaned_data['Intelligence']
            character.WIS_score = form.cleaned_data['Wisdom']
            character.CHA_score = form.cleaned_data['Charisma']

            character.save()

            request.session['character'] = character.pk

            return redirect('nc_personality')

        return render(request, 'characters/nc_ability_scores.html', context)


@login_required()
def nc_personality(request):
    """Get information about the character's personality."""

    if request.method == "GET":

        form = CCPersonality()
        class_level = ClassLevel.objects.filter(character__pk=request.session['character'])
        character = Character.objects.get(pk=request.session['character'])

        context = {'character': character, 'class_level': class_level, 'form': form}

        return render(request, 'characters/nc_personality.html', context)

    elif request.method == "POST":
        form = CCPersonality(data=request.POST)
        class_level = ClassLevel.objects.filter(character__pk=request.session['character'])
        character = Character.objects.get(pk=request.session['character'])

        context = {'character': character, 'class_level': class_level, 'form': form}

        if form.is_valid():

            character.alignment = form.cleaned_data['alignment']

            if form.cleaned_data['ideals'] != "":
                character.ideals = form.cleaned_data['ideals']

            if form.cleaned_data['bonds'] != "":
                character.ideals = form.cleaned_data['bonds']

            if form.cleaned_data['flaws'] != "":
                character.ideals = form.cleaned_data['flaws']

            character.save()

            return redirect('nc_background')

        return render(request, 'characters/nc_personality.html', context)


@login_required()
def nc_background(request):
    """Assign the character's background."""

    if request.method == "GET":
        form = CCBackground()
        class_level = ClassLevel.objects.filter(character__pk=request.session['character'])
        character = Character.objects.get(pk=request.session['character'])

        context = {'character': character, 'class_level': class_level, 'form': form}

        return render(request, 'characters/nc_background.html', context)

    elif request.method == "POST":
        form = CCBackground(data=request.POST)
        class_level = ClassLevel.objects.filter(character__pk=request.session['character'])
        character = Character.objects.get(pk=request.session['character'])

        context = {'character': character, 'class_level': class_level, 'form': form}

        if form.is_valid():
            character.char_background = form.cleaned_data['background']

            character.save()

            return redirect('nc_equipment')

        return render(request, 'characters/nc_background.html', context)


@login_required()
def nc_equipment(request):
    """Assigning starting equipment"""

    if request.method == "GET":
        form = CCEquipment()
        class_level = ClassLevel.objects.filter(character__pk=request.session['character'])
        character = Character.objects.get(pk=request.session['character'])

        context = {'character': character, 'class_level': class_level, 'form': form}

        return render(request, 'characters/nc_equipment.html', context)

    elif request.method == "POST":
        form = CCEquipment(data=request.POST)
        class_level = ClassLevel.objects.filter(character__pk=request.session['character'])
        character = Character.objects.get(pk=request.session['character'])

        context = {'character': character, 'class_level': class_level, 'form': form}

        if form.is_valid():
            character.weapons_inv = form.cleaned_data['weapons']
            character.tools_inv = form.cleaned_data['tools']
            character.items_inv = form.cleaned_data['items']
            character.armor_inv = form.cleaned_data['armor']

            character.save()

            return redirect('nc_resolve')

        return render(request, "characters/nc_resolve.html", context)


@login_required()
def nc_resolve(request):
    """Final screen for character. Show all information and as where they want to go next."""

    if request.method == "GET":
        form = NCResolve()
        class_level = ClassLevel.objects.filter(character__pk=request.session['character'])
        character = Character.objects.get(pk=request.session['character'])

        context = {'character': character, 'class_level': class_level, 'form': form}

        return render(request, "characters/nc_resolve.html", context)

    elif request.method == "POST":

        form = NCResolve(data=request.POST)

        context = {'form': form}

        if form.is_valid():

            next_page = form.cleaned_data['next_page']

            if next_page == "delete":
                Character.objects.get(pk=request.session['character']).delete()
                next_page = "home"

            elif next_page == "":
                next_page = "home"

            request.session['character'] = ''

            # context = dict()

            return redirect(next_page)

        return render(request, "characters/nc_resolve.html", context)
