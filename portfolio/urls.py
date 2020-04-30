from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name="mainhome"),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('portfolio/home.html', views.home, name='portfolio'),
    path('morse/', views.morsePage, name='morse'),
    path('todonfire/', views.todoonfirePage, name='todonfire'),
    path('scampy/', views.scampyPage, name='scampy'),

    path('blog/', views.PostListView.as_view(), name='blog'),
    path('blog/new/', views.post_new, name='blog_new'),
]
