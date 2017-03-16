"""
All the views that a user will see on the site.
"""


# Python Imports:
import re


# Django Imports:
from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages

# Module and Form Imports:
from .forms import SearchDatabase

# Model Imports:
from rules.models import (Alignment, Class, PrestigeClass, Race, Subrace, DamageType, Feature, Skill)
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
            model_name = re.findall(r'[A-Z]\w+', str(model))[0]

            if found and model_name[-1] == 's':
                model_name += 'es'
                results[model_name] = list()
                for name in found:
                    results[model_name].append(name.name)
                    total += 1

            elif found and model_name[-1] != 's':
                model_name += 's'
                results[model_name] = list()
                for name in found:
                    results[model_name].append(name.name)
                    total += 1

    context = {'query': query, 'results': results, 'total': total}

    return render(request, 'database_view/search_home.html', context)
