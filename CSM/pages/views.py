from django.shortcuts import render

# Create your views here.

def landing(request):

    context = dict()

    return render(request, 'landing.html', context)

