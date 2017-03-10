from django.shortcuts import render
from django.db.models import Q


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SpellModelSerializer
from spells.models import Spell
from .forms import SearchSpells

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

    if bool(query_spell) == True:
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