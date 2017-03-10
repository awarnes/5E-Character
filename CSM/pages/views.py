from django.shortcuts import render
from django.db.models import Q


# Create your views here.


def landing(request):

    context = dict()

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