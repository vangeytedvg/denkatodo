"""
"  views.py
"  Author  : Danny Van Geyte
"  Purpose : define django views
"  File date : 22/04/2020
"
"""
from django.shortcuts import render, redirect
from .models import Todo, TaskUser, ArchivedTodo
from django.contrib.auth import authenticate, login, logout
from .forms import TodoForm, CreateUserForm, DispatcherForm
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .decorators import unauthenticated_user

# ---- MAIN PAGE


def mainhome(request):
    return redirect('portfolio/home.html')

@login_required(login_url='login')
def home(request):
    print("HOME REQUESTED")
    """ Home Page of the application """
    # How to filter only the task for this user
    todos = Todo.objects.all().filter(task_owner=request.user.id).order_by('-id')
    # This the trick to set the default user in the task_owner
    # listbox!
    form = TodoForm()
    print(request.user.is_superuser)
    if request.method == "POST":
        form = TodoForm(initial={'task_owner': request.user})

    lasttodo = Todo.objects.last()
    context = {'todos': todos, 'lasttodo': lasttodo, 'form': form}
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


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            TaskUser.objects.create(
                user=user,
                name=user.username,
                email=user.email,
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'main/register.html', context)


# ---- This section contains the views for managing todos
@login_required(login_url='login')
def addTodo(request):
    print("ADD REQUESTED")
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            t.task_owner_id = request.user.id
            t.status = "OP"
            t.save()
            return redirect('/')
    currentUser = request.user
    context = {'form': form, 'currentUser': currentUser}
    return render(request, 'main/home.html', context)


@login_required(login_url='login')
def deleteCompleted(request):
    # Remove all tasks marked with 'DN' (Done), for the current logged user
    current_user = request.user.id
    xterminate = Todo.objects.filter(status='DN', task_owner=current_user)  # .delete()
    # Before we remove items, we put them in the archive bin
    for item in xterminate:
        arch = ArchivedTodo()
        arch.task = item.task
        arch.status = "DN"
        arch.task_owner = item.task_owner
        arch.date_created = item.date_created
        arch.date_closed = item.date_closed
        arch.save()
        item.delete()
    messages.success(request, "Completed records were removed!")
    return redirect('home')


@login_required(login_url='login')
def deleteAll(request):
    return redirect('home')


@login_required(login_url='login')
def completeTodo(request, todo_id):
    # ---- Mark a todo as done
    todo = Todo.objects.get(pk=todo_id)
    todo.date_closed = datetime.now()
    print(datetime.now())
    todo.status = "DN"
    todo.save()
    return redirect('home')


@login_required(login_url='login')
def inprogressTodo(request, todo_id):
    # ---- Mark a todo as in progress
    todo = Todo.objects.get(pk=todo_id)
    todo.status = "IP"
    todo.save()
    return redirect('home')


@login_required(login_url='login')
def recallTodo(request, todo_id):
    # ---- Mark a todo as done
    todo = Todo.objects.get(pk=todo_id)
    todo.status = "OP"
    todo.save()
    return redirect('home')


@login_required(login_url='login')
def reopenClosed(request, todo_id):
    # ---- Mark a todo as done
    todo = Todo.objects.get(pk=todo_id)
    todo.status = "OP"
    todo.save()
    return redirect('home')


# ---- ARCHIVE PAGE
@login_required(login_url='login')
def archive(request):
    todos = ArchivedTodo.objects.all().filter(task_owner=request.user.id).order_by('date_closed')
    context = {'archive': todos}
    return render(request, 'main/archive.html', context)


# ---- Admin pages
@login_required(login_url='login')
def settings(request):
    users = User.objects.all().order_by('username')
    context = {'users': users}

    return render(request, 'main/settings.html', context)


@login_required(login_url='login')
def getUserTodos(request, user_id):
    tu = TaskUser.objects.get(pk=user_id)
    ll = Todo.objects.all().filter(task_owner=user_id)
    context = {'usertodos': ll, 'tuser': tu}
    return render(request, 'main/userTodos.html', context)


@login_required(login_url='login')
def dispatchTodo(request):
    # ---- Admin dispatching of tasks
    usertodos = Todo.objects.all().order_by('-id')
    form = DispatcherForm()
    if request.method == "POST":
        form = DispatcherForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form, 'usertodos': usertodos}
    return render(request, 'main/dispatcher.html', context)
