from django.urls import path
from . import views
urlpatterns = [
    path('add/',views.AddPost,name="AddPost"),
    path('edit/<int:id>',views.EditPost,name="EditPost"),
    path('delete/<int:id>',views.DeletePost,name="DeletePost")
]