from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse

from spells.models import Spell
from .forms import SearchSpells

# Create your views here.


def landing(request):

    context = dict()

    return render(request, 'landing.html', context)


def spell_book(request):
    """Searches all spells and displays ones queried."""

    if request.method == 'GET':
        form = SearchSpells()
        spells = Spell.objects.all()

    elif request.method == 'POST':
        query = request.POST.get('query')
        if query == None:
            query = ''
        form = SearchSpells(data=request.POST)
        spells = Spell.objects.filter(Q(name__icontains=query) | Q(available_to__icontains=query))

    context = {'spells': spells, 'form': form}

    return render(request, 'spellbook.html', context)

def get_spell_information(request):

    spell = str()

    if request.method == 'GET':
        query_spell = request.GET.get('spell')
        spell = Spell.objects.filter(name__icontains=query_spell)

    return JsonResponse({'name': spell[0].name, 'level': spell[0].level, 'school': spell[0].school, 'cast_time': spell[0].cast_time,
                         'distance': spell[0].distance, 'components': spell[0].raw_materials, 'duration': spell[0].duration,
                         'concentration': spell[0].concentration, 'ritual': spell[0].ritual, 'description': spell[0].description,
                         'available_to': spell[0].available_to})