from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about),
    path('contact/',views.contact)
]