from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name='logout'),

    path('reset_password',
         auth_views.PasswordResetView.as_view(
             template_name="main/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent',
         auth_views.PasswordResetDoneView.as_view(
             template_name="main/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="main/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="main/password_reset_done.html"),
         name="password_reset_complete"),


    path('dispatch', views.dispatchTodo, name='dispatch'),

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
