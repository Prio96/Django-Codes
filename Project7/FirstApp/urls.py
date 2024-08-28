from django.urls import path
from FirstApp.views import home

urlpatterns = [
    path('',home,name="homepage")
]