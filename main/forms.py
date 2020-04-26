
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

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
        exclude = ['task_owner', 'status', 'date_closed']


class DispatcherForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['date_closed']


class CreateUserForm(UserCreationForm):
    """
        "  Purpose    : Create a new user
        "  Parameters : na
        "  returns    : na
        """
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
