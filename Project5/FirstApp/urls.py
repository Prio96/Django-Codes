from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="homepage"),
    path('about/',views.about,name="aboutpage"),
    path('form/',views.form,name="form-submit")
]

#name is used to make things easier while giving a link in html file(In this case, base.html). It is used with url template tag like{% url 'name' %} in href