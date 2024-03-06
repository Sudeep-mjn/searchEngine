from django.contrib import admin
from django.urls import path
from scrapper import views

urlpatterns = [
    path("", views.index),
    
]
