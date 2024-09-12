from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="HomePage"),
    path('signup/',views.make_acc,name="signup"),
    path('signin/',views.user_login,name="login"),
    path('profile/',views.user_profile,name="profile"),
    path('logout/',views.user_logout,name="logout"),
    path('changepass1/',views.pass_change1,name="changepass1"),
    path('changepass2/',views.pass_change2,name="changepass2"),
]