from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('base', views.base,name='base'),
    path('about', views.about,name='about'),
    path('join', views.join,name='join'),
    path('<str:slug>', views.blogpost, name='blogpost'),
]
