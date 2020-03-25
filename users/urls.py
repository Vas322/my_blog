"""Определяет схемы URL для пользователей"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import logout
from django.contrib.auth import login

app_name = 'users'
urlpatterns = [
    # Страница входа
    path('users/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # Страница выхода
    path(r'logout/', views.logout_view, name='logout'),
    # Страница регистрации
    path(r'register/', views.register, name='register'),
]
