"""
All the views that a user will see on the site.
"""


# Django Imports:
from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages

# Module and Form Imports:
from .forms import SearchDatabase


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
        form = SearchDatabase()

    context = {'form': form}

    return render(request, 'database_view/search_home.html', context)
