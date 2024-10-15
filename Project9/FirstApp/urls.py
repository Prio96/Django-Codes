from django.urls import path
from .views import home,get_cookie,del_cookie
urlpatterns = [
    path('',home),
    path('get/',get_cookie),
    path('del/',del_cookie)
]