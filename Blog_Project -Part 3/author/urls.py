from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/',views.Register,name="Register"),
    path('login/',views.AuthorLoginView.as_view(),name="Login"),
    path('profile/',views.Profile,name="Profile"),
    path('logout/',LogoutView.as_view(http_method_names=['get','post']),name="Logout"),
    path('profile/editprofile/passchange/',views.Pass_Change,name="ChangePass"),
    path('profile/editprofile/',views.Edit_Profile,name="EditProfile"),
]