"""
" Porfolio/views.py
"
"""

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Blog, Visitors
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostForm


class PostListView(ListView):
    # Return the ten last blog items
    model = Blog 
    template_name = 'blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Blog.objects.filter(status=1).order_by('-date_created')[:10]

def mainpage(request):
    return redirect('portfolio/home.html')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_new')
    else:
        form = PostForm()
    return render(request, 'create_blog_item.html', {'form': form})

def PostList(request):
    queryset = Blog.objects.filter(status=1).order_by('-date_created')
    context = {'post_list': queryset}
    return render (request, 'blog.html', context)


def home(request):
    """ Home Page of the application """
    # How to filter only the task for this user
    # Implemented a visitor counter in the application
    pageCounter = Visitors.objects.all().count()
    if pageCounter == 0:
        # Create new counter
        new_entry=Visitors(counter=0)
        new_entry.save()
    pageCounter = Visitors.objects.get(pk=1)
    pageCounter.counter += 1
    pageCounter.save()
    

    context = {}
    return render(request, 'home.html', context)


def aboutme(request):
    context = {}
    return render(request, 'aboutme.html', context)


def morsePage(request):
    context = {}
    return render(request, 'morse.html', context)


def todoonfirePage(request):
    context = {}
    return render(request, 'todoonfire.html', context)


def scampyPage(request):
    context = {}
    return render(request, 'scampy.html', context)

@login_required(login_url='login')
def stats(request):
    print(request)
    stats = Visitors.objects.get(pk=1)
    context = {'stats': stats}
    return render(request, 'statistics.html', context)

