from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name='logout'),

    path('dispatch/', views.dispatchTodo, name='dispatch'),

    path('add/', views.addTodo, name='add'),
    path('complete/<str:todo_id>', views.completeTodo, name='complete'),
    path('recall/<str:todo_id>', views.recallTodo, name='recall'),
    path('inprogressTodo/<todo_id>', views.inprogressTodo, name='inprogressTodo'),
    path('deletecomplete/', views.deleteCompleted, name='deletecomplete'),
    path('deleteall/', views.deleteAll, name='deleteall'),
    path('detailuser/<str:user_id>/', views.getUserTodos, name='detailuser'),
    path('archive', views.archive, name='archive'),

    path('settings', views.settings, name='settings')
]
