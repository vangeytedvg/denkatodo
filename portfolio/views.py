from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    """ Home Page of the application """
    # How to filter only the task for this user

    context = {}
    return render(request, 'home.html', context)


def aboutme(request):
    context = {}
    return render(request, 'aboutme.html', context)
