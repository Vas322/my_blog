"""Определяет схемы URL для blogs."""
from django.urls import path
from . import views

app_name = 'blogs'


urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # страница со всеми постами
    path(r'posts/', views.posts, name='posts'),
    # Страница с подробной информацией по отдельной теме
    path(r'posts/<post_id>/', views.post, name='post'),
    # Страница для добавления нового поста
    path(r'new_post/', views.new_post, name='new_post'),
    # Страница для добавления новой записи
    path(r'new_entry/(<post_id>)/', views.new_entry, name='new_entry'),
    # Страница для редактирования записи
    path(r'edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
]
