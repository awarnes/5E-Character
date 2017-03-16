# Django Imports:
from django.shortcuts import render
from django.db.models import Q


# DRF Imports:
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

# Serializer and Form Imports:
from .serializers import (SpellModelSerializer, CharacterModelSerializer, SkillModelSerializer, SubraceModelSerializer,
                          RaceModelSerializer, PrestigeClassModelSerializer, ClassModelSerializer, FeatureModelSerializer,
                          BackgroundModelSerializer, LanguageModelSerializer, ConditionModelSerializer, DamageTypeModelSerializer,
                          AlignmentModelSerializer, WeaponModelSerializer, WeaponPropertyModelSerializer, ItemModelSerializer,
                          ToolModelSerializer, ArmorModelSerializer, MountAndVehicleModelSerializer)


from .forms import SearchSpells #SearchUserCharacters

# Model Imports:
from spells.models import Spell
from character.models import Character
from accounts.models import Member
from equipment.models import Weapon, WeaponProperty, Armor, Item, Tool, MountAndVehicle
from rules.models import (Subrace, Race, PrestigeClass, Class, Feature, Background,
                          Skill, Language, DamageType, Condition, Alignment)


# Rule API endpoints:
class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows skills to be viewed.
    """

    queryset = Skill.objects.all()
    serializer_class = SkillModelSerializer


class SubraceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows subraces to be viewed.
    """

    queryset = Subrace.objects.all()
    serializer_class = SubraceModelSerializer


class RaceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows races to be viewed.
    """

    queryset = Race.objects.all()
    serializer_class = RaceModelSerializer


class PrestigeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows prestige classes to be viewed.
    """

    queryset = PrestigeClass.objects.all()
    serializer_class = PrestigeClassModelSerializer


class ClassViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows classes to be viewed.
    """

    queryset = Class.objects.all()
    serializer_class = ClassModelSerializer


class FeatureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows features to be viewed.
    """

    queryset = Feature.objects.all()
    serializer_class = FeatureModelSerializer


class BackgroundViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows backgrounds to be viewed.
    """

    queryset = Background.objects.all()
    serializer_class = BackgroundModelSerializer


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows languages to be viewed.
    """

    queryset = Language.objects.all()
    serializer_class = LanguageModelSerializer


class ConditionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows conditions to be viewed.
    """

    queryset = Condition.objects.all()
    serializer_class = ConditionModelSerializer


class DamageTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows damage types to be viewed.
    """

    queryset = DamageType.objects.all()
    serializer_class = DamageTypeModelSerializer


class AlignmentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows alignment to be viewed.
    """

    queryset = Alignment.objects.all()
    serializer_class = AlignmentModelSerializer


# Equipment API endpoints:
class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows items to be viewed.
    """

    queryset = Item.objects.all()
    serializer_class = ItemModelSerializer


class ToolViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows tools to be viewed.
    """

    queryset = Tool.objects.all()
    serializer_class = ToolModelSerializer


class WeaponViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows weapons to be viewed.
    """

    queryset = Weapon.objects.all()
    serializer_class = WeaponModelSerializer


class ArmorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows armor to be viewed.
    """

    queryset = Armor.objects.all()
    serializer_class = ArmorModelSerializer


class WeaponPropertyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows weapon properties to be viewed.
    """

    queryset = WeaponProperty.objects.all()
    serializer_class = WeaponPropertyModelSerializer


class MountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows mounts and vehicles to be viewed.
    """

    queryset = MountAndVehicle.objects.all()
    serializer_class = MountAndVehicleModelSerializer


# Spell API endpoints:
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


# Character API endpoints:
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