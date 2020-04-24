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
from django.contrib.auth.forms import UserCreationForm
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.views.decorators.http import require_POST
from .forms import TodoForm, CreateUserForm

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
            t = form.save(commit=False)
            t.task_owner_id = request.user.id
            t.status = "OP"
            t.save()
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


@login_required(login_url='login')
def deleteCompleted(request):
    # Remove all tasks marked with 'DN' (Done), for the current logged user
    current_user = request.user.id
    Todo.objects.filter(status='DN', task_owner=current_user).delete()
    messages.success(request, "Completed records were removed!")
    return redirect('home')


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='todomaker')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'main/register.html', context)


@login_required(login_url='login')
def deleteAll(request):
    return redirect('home')


@login_required(login_url='login')
def completeTodo(request, todo_id):
    # ---- Mark a todo as done
    todo = Todo.objects.get(pk=todo_id)
    todo.status = "DN"
    todo.save()
    return redirect('home')


@login_required(login_url='login')
def inprogressTodo(request, todo_id):
    # ---- Mark a todo as done
    todo = Todo.objects.get(pk=todo_id)
    todo.status = "IP"
    todo.save()
    return redirect('home')
