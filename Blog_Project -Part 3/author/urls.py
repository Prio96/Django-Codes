from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.Register,name="Register"),
    path('login/',views.Log_in,name="Login"),
    path('profile/',views.Profile,name="Profile"),
    path('logout/',views.Logout,name="Logout"),
    path('profile/editprofile/passchange/',views.Pass_Change,name="ChangePass"),
    path('profile/editprofile/',views.Edit_Profile,name="EditProfile"),
]