from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

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

# def display_spell(request):
#
#     spell