from django.urls import path
from . import views
urlpatterns = [
    path('add/',views.AddPostClassView.as_view(),name="AddPost"),
    path('edit/<int:id>',views.EditPostClassView.as_view(),name="EditPost"),
    path('delete/<int:id>',views.DeletePostClassView.as_view(),name="DeletePost")
]