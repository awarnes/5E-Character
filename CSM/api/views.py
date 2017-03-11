# Django Imports:
from django.shortcuts import render
from django.db.models import Q

# DRF Imports:
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Serializer and Form Imports:
from .serializers import SpellModelSerializer, CharacterModelSerializer
from .forms import SearchSpells #SearchUserCharacters

# Model Imports:
from spells.models import Spell
from character.models import Character
from accounts.models import Member

# Create your views here.


# class SpellViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows spells to be viewed.
#     """
#
#     queryset = Spell.objects.all()
#     serializer_class = SpellModelSerializer

@api_view(['GET'])
def get_spell_information(request):
    """
    API endpoint to get information on a SINGLE spell.
    """

    query_spell = request.GET.get('query_spell')
    spell = Spell.objects.filter(name__icontains=query_spell)

    serializer = SpellModelSerializer(spell, many=True)

    if bool(spell) == True:
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def spell_book(request):
    """API endpoint searches ALL spells and displays ones queried."""

    if request.method == 'GET':
        form = SearchSpells()
        spells = Spell.objects.all()
        spells_1 = spells[:len(spells) // 3]
        spells_2 = spells[len(spells) // 3:(len(spells) // 3) * 2]
        spells_3 = spells[(len(spells) // 3) * 2:]

    elif request.method == 'POST':
        query = request.POST.get('query')
        if query == None:
            query = ''
        form = SearchSpells(data=request.POST)
        spells = Spell.objects.filter(Q(name__icontains=query) | Q(available_to__icontains=query))
        spells_1 = spells[:len(spells) // 3]
        spells_2 = spells[len(spells) // 3:(len(spells) // 3) * 2]
        spells_3 = spells[(len(spells) // 3) * 2:]

    context = {'spells1': spells_1, 'spells2': spells_2, 'spells3': spells_3, 'form': form}

    return render(request, 'spellbook.html', context)


@api_view(['GET'])
def user_character_names(request):
    """Returns all characters' names for a single user."""

    member = request.user

    member_characters = member.characters.values_list('char_name')

    context = {'characters': member_characters}

    if bool(member_characters):
        return Response(context, status=status.HTTP_200_OK)
    else:
        return Response(context, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def specific_user_character(request):
    """Returns a specific character for a user"""

    member = request.user

    query_char = request.GET.get('query_char')

    character = member.characters.filter(char_name=query_char)

    serializer = CharacterModelSerializer(character, many=True)

    if bool(character) == True:
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)