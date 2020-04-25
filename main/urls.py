from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name='logout'),

    path('add/', views.addTodo, name='add'),
    path('complete/<str:todo_id>', views.completeTodo, name='complete'),
    path('recall/<str:todo_id>', views.recallTodo, name='recall'),
    path('inprogressTodo/<todo_id>', views.inprogressTodo, name='inprogressTodo'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall'),

    path('archive', views.archive, name='archive'),

    path('settings', views.settings, name='settings')
]
