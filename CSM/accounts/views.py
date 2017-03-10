from django.shortcuts import render
from django.contrib.auth import logout

from .forms import MemberCreateForm


"""
from django.contrib.auth.decorators import login_required

@login_required
"""

# Create your views here.


# May want to keep this for later...
# def user_login(request):
#     """
#     Logs in a currently active user.
#     """
#
#
#     if request.method == 'GET':
#         form = UserLoginForm()
#         context = {'form': form}
#
#     elif request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#
#             user = authenticate(username=username, password=password)
#
#             context = {'user': user}
#
#             if user is not None:
#                 login(request, user)
#
#                 return render(request, 'accounts/user_home.html', context)
#
#             else:
#
#                 return render(request, 'accounts/invalid_login.html', context)
#
#     return render(request, 'accounts/login.html', context)
#
#
def user_logout(request):
    """
    Logs out a currently active user.
    """

    context = {'user': request.GET.get('user')}

    logout(request)

    return render(request, 'accounts/logged_out.html', context)


def user_home(request):

    context = dict()

    return render(request, 'accounts/user_home.html', context)


def register_user(request):
    """
    Registers a new user in the system with base permissions.
    """

    if request.method == 'GET':
        form = MemberCreateForm()
        context = {'form': form}

    elif request.method == 'POST':
        form = MemberCreateForm(data=request.POST)
        context = {'form': form}

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            return render(request, 'accounts/register_success.html', context)

        else:

            return render(request, 'accounts/register.html', context)

    return render(request, 'accounts/register.html', context)
