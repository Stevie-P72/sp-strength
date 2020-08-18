from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('view/<str:article_name>/', views.article, name='article'),
    path('edit/<str:article_name>/', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('delete/<str:article_name>/', views.delete, name='delete'),
]
