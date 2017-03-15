from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages

# Create your views here.


def landing(request):

    context = dict()

    messages.info(request, "Hello there! Welcome!")

    return render(request, 'landing.html', context)

def about_us(request):
    """
    Basic contact form for web page.
    """

    context = {'title': 'About Us!'}

    return render(request, 'about_us.html', context)

def report_issue(request):
    """
    Basic contact form for web page.
    """

    context = {'title': 'Report an Issue!'}

    return render(request, 'report_issue.html', context)