"""
All the views that a user will see on the site.
"""


# Python Imports:
import re


# Django Imports:
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib import messages

# Module and Form Imports:
from .forms import SearchDatabase

# Model Imports:
from rules.models import (Alignment, Class, PrestigeClass, Race, Subrace, DamageType, Feature, Skill, Background,
                          Language, Condition, )
from spells.models import Spell
from character.models import Character
from equipment.models import (Weapon, Armor, Tool, Item, MountAndVehicle)


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
                  Skill, Alignment, DamageType, MountAndVehicle)
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


def spell_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    spell = get_object_or_404(Spell, slug=slug)

    classes = list()
    for klass in spell.available_to.split(', '):
        if klass != '':
            classes.append(klass)

    context = {'result': spell, 'classes': classes}

    return render(request, 'database_view/detail_pages/spell_details.html', context)


def subrace_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    subrace = get_object_or_404(Subrace, slug=slug)

    context = {'result': subrace}

    return render(request, 'database_view/detail_pages/subrace_details.html', context)


def race_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    race = get_object_or_404(Race, slug=slug)

    context = {'result': race}

    return render(request, 'database_view/detail_pages/race_details.html', context)


def prestige_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    prestige = get_object_or_404(PrestigeClass, slug=slug)

    context = {'result': prestige}

    return render(request, 'database_view/detail_pages/prestige_details.html', context)


def class_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    klass = get_object_or_404(Class, slug=slug)

    context = {'result': klass}

    return render(request, 'database_view/detail_pages/class_details.html', context)


def feature_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    feature = get_object_or_404(Feature, slug=slug)

    context = {'result': feature}

    return render(request, 'database_view/detail_pages/feature_details.html', context)


def background_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    background = get_object_or_404(Background, slug=slug)

    context = {'result': background}

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

    context = {'result': weapon}

    return render(request, 'database_view/detail_pages/weapon_details.html', context)


def armor_details(request, slug):
    """
    Detail HTML for Spell instances
    """
    armor = get_object_or_404(Armor, slug=slug)

    context = {'result': armor}

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

    context = {'result': mount}

    return render(request, 'database_view/detail_pages/mount_details.html', context)

