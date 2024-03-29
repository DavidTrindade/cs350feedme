from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('favourites/', views.faves, name='faves'),
    path('favourite/<int:id>', views.fav, name='fav'),
    path('feed/<int:id>', views.feed, name='feed'),
    path('graph/', views.graph, name='graph'),
]