from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutme', views.aboutme, name='aboutme'),
    path('morse', views.morsePage, name='morse'),
    path('todonfire', views.todoonfirePage, name='todonfire'),
    path('scampy', views.scampyPage, name='scampy')
]
