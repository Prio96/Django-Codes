from django.urls import path
from .views import home,get_cookie,del_cookie,set_session,get_session,del_session
urlpatterns = [
    path('',home),
    path('get/',get_cookie),
    path('del/',del_cookie),
    path('set_session/',set_session),
    path('get_session/',get_session),
    path('del_session/',del_session)
]