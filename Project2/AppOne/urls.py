from django.urls import path
# from AppOne.views import home
# from AppOne import views
from . import views
urlpatterns = [
    path('',views.home)
]