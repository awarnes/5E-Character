# Django Imports:
from django.shortcuts import render
from django.db.models import Q


# DRF Imports:
from rest_framework import status
from rest_framework.decorators import api_view, detail_route
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
from equipment.models import (Weapon, WeaponProperty, Armor, Item, Tool, MountAndVehicle)
from rules.models import (Subrace, Race, PrestigeClass, Class, Feature, Background,
                          Skill, Language, DamageType, Condition, Alignment)


# Rule API endpoints:
class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows skills to be viewed.
    """

    queryset = Skill.objects.all()
    serializer_class = SkillModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def skill_detail(self, slug=None):
        skill = Skill.objects.filter(name__icontains=slug)

        serializer = SkillModelSerializer(skill, many=False)

        if bool(skill):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class SubraceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows subraces to be viewed.
    """

    queryset = Subrace.objects.all()
    serializer_class = SubraceModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def subrace_detail(self, slug=None):
        subrace = Subrace.objects.filter(name__icontains=slug)

        serializer = SubraceModelSerializer(subrace, many=False)

        if bool(subrace):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class RaceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows races to be viewed.
    """

    queryset = Race.objects.all()
    serializer_class = RaceModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def race_detail(self, slug=None):
        race = Race.objects.filter(name__icontains=slug)

        serializer = RaceModelSerializer(race, many=False)

        if bool(race):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class PrestigeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows prestige classes to be viewed.
    """

    queryset = PrestigeClass.objects.all()
    serializer_class = PrestigeClassModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def prestige_detail(self, slug=None):
        prestige = PrestigeClass.objects.filter(name__icontains=slug)

        serializer = PrestigeClassModelSerializer(prestige, many=False)

        if bool(prestige):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class ClassViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows classes to be viewed.
    """

    queryset = Class.objects.all()
    serializer_class = ClassModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def class_detail(self, slug=None):
        klass = Class.objects.filter(name__icontains=slug)

        serializer = ClassModelSerializer(klass, many=False)

        if bool(klass):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class FeatureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows features to be viewed.
    """

    queryset = Feature.objects.all()
    serializer_class = FeatureModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def feature_detail(self, slug=None):
        feature = Feature.objects.filter(name__icontains=slug)

        serializer = FeatureModelSerializer(feature, many=False)

        if bool(feature):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class BackgroundViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows backgrounds to be viewed.
    """

    queryset = Background.objects.all()
    serializer_class = BackgroundModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def background_detail(self, slug=None):
        background = Background.objects.filter(name__icontains=slug)

        serializer = BackgroundModelSerializer(background, many=False)

        if bool(background):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows languages to be viewed.
    """

    queryset = Language.objects.all()
    serializer_class = LanguageModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def language_detail(self, slug=None):
        language = Language.objects.filter(name__icontains=slug)

        serializer = LanguageModelSerializer(language, many=False)

        if bool(language):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class ConditionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows conditions to be viewed.
    """

    queryset = Condition.objects.all()
    serializer_class = ConditionModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def condition_detail(self, slug=None):
        condition = Condition.objects.filter(name__icontains=slug)

        serializer = AlignmentModelSerializer(condition, many=False)

        if bool(condition):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class DamageTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows damage types to be viewed.
    """

    queryset = DamageType.objects.all()
    serializer_class = DamageTypeModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def damage_type_detail(self, slug=None):
        damage_type = DamageType.objects.filter(name__icontains=slug)

        serializer = DamageTypeModelSerializer(damage_type, many=False)

        if bool(damage_type):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class AlignmentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows alignment to be viewed.
    """

    queryset = Alignment.objects.all()
    serializer_class = AlignmentModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def alignment_detail(self, slug=None):
        alignment = Alignment.objects.filter(name__icontains=slug)

        serializer = AlignmentModelSerializer(alignment, many=False)

        if bool(alignment):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


# Equipment API endpoints:
class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows items to be viewed.
    """

    queryset = Item.objects.all()
    serializer_class = ItemModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def item_detail(self, slug=None):
        item = Item.objects.filter(name__icontains=slug)

        serializer = ItemModelSerializer(item, many=False)

        if bool(item):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

class ToolViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows tools to be viewed.
    """

    queryset = Tool.objects.all()
    serializer_class = ToolModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def tool_detail(self, slug=None):
        tool = Tool.objects.filter(name__icontains=slug)

        serializer = ToolModelSerializer(tool, many=False)

        if bool(tool):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class WeaponViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows weapons to be viewed.
    """

    queryset = Weapon.objects.all()
    serializer_class = WeaponModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def weapon_detail(self, slug=None):
        weapon = Weapon.objects.filter(name__icontains=slug)

        serializer = WeaponModelSerializer(weapon, many=False)

        if bool(weapon):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class ArmorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows armor to be viewed.
    """

    queryset = Armor.objects.all()
    serializer_class = ArmorModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def armor_detail(self, slug=None):
        armor = Armor.objects.filter(name__icontains=slug)

        serializer = ArmorModelSerializer(armor, many=False)

        if bool(armor):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class WeaponPropertyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows weapon properties to be viewed.
    """

    queryset = WeaponProperty.objects.all()
    serializer_class = WeaponPropertyModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def weapon_property_detail(self, slug=None):
        weapon_property = WeaponProperty.objects.filter(name__icontains=slug)

        serializer = WeaponPropertyModelSerializer(weapon_property, many=False)

        if bool(weapon_property):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class MountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows mounts and vehicles to be viewed.
    """

    queryset = MountAndVehicle.objects.all()
    serializer_class = MountAndVehicleModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def mount_detail(self, slug=None):
        mount = MountAndVehicle.objects.filter(name__icontains=slug)

        serializer = MountAndVehicleModelSerializer(mount, many=False)

        if bool(mount):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


# Spell API endpoints:
class SpellViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to get information on a SINGLE spell.
    """
    queryset = Spell.objects.all()
    serializer_class = SpellModelSerializer
    lookup_field = 'slug'

    @detail_route(methods=['GET'])
    def spell_detail(self, slug=None):
        spell = Spell.objects.filter(name__icontains=slug)

        serializer = SpellModelSerializer(spell, many=True)

        if bool(spell):
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

    return render(request, 'database_view/spellbook.html', context)


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