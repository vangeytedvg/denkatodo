"""
"  views.py
"  Author  : Danny Van Geyte
"  Purpose : define django views
"  File date : 22/04/2020
"
"""
from django.shortcuts import render, redirect
from .models import Todo, TaskUser
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.views.decorators.http import require_POST
from .forms import TodoForm

# Create your views here.


@login_required(login_url='login')
def home(request):
    """ Home Page of the application """
    print(request.user)
    # How to filter only the task for this user
    todos = Todo.objects.all().filter(task_owner=request.user.id).order_by('-id')
    # This the trick to set the default user in the task_owner
    # listbox!
    form = TodoForm(initial={'task_owner': request.user})

    lasttodo = Todo.objects.last()

    context = {'todos': todos, 'lasttodo': lasttodo, 'form': form}

    return render(request, 'main/home.html', context)


@login_required(login_url='login')
def addTodo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    currentUser = request.user
    context = {'form': form, 'currentUser': currentUser}
    return render(request, 'main/home.html', context)


@unauthenticated_user
def loginPage(request):
    """
        Purpose    : Let a user log in
        Parameters : request
        Returns    : 'main/login.html'
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        # this is according to the django documentation
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'main/login.html', context)


def logoutUser(request):
    """
        Purpose    : Hasta la vista baby
        Parameters : name
        Returns    : 'login'
    """
    logout(request)
    return redirect('login')

# ---- This section contains the views for managing todos


def deleteCompleted(request):
    return redirect('home')


def deleteAll(request):
    return redirect('home')


def completeTodo(request, pk):
    return redirect('home')
