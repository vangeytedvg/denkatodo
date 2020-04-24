
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class TodoForm(ModelForm):
    """
    "  Purpose The todo entry form
    "  Parameters na
    "  returns na
    """
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['task_owner', 'status']


class CreateUserForm(UserCreationForm):
    """
        "  Purpose    : Create a new user
        "  Parameters : na
        "  returns    : na
        """
    class Meta:
        model = User
        # If we set __all__ here, we get trouble because there are much
        # more fields than needed, if these four are set, the system only
        # checks these four!
        fields = ['username', 'email', 'password1', 'password2']
