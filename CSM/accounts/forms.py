from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Member


class MemberCreateForm(UserCreationForm):
    """
    Creates a user in the database with username, password, email, and ok_to_contact.
    """

    email = forms.EmailField(required=True)
    ok_to_contact = forms.BooleanField(required=False)

    class Meta(UserCreationForm.Meta):
        model = Member
        fields = UserCreationForm.Meta.fields + ('email', 'ok_to_contact',)


# class UserLoginForm(ModelForm):
#     """
#     Form for logging into the website.
#     """
#
#     class Meta:
#         model = Member
#         fields = ('username', 'password',)