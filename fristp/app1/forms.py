from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms
from django.forms.widgets import PasswordInput, TextInput



class CreateUserForm(UserCreationForm):

    class Meta:
        model = User  
        fields = ['username', 'email', 'password1', 'password2']


# Authentication

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput( ))
    password = forms.CharField(widget=PasswordInput())