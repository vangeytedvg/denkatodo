from django.shortcuts import render
from .models import Todo, TaskUser


# Create your views here.
def home(request):
    """ Home Page of the application """
    todos = Todo.objects.all()
    lasttodo = Todo.objects.last()

    context = {'todos': todos, 'lasttodo': lasttodo}

    return render(request, 'main/home.html', context)
