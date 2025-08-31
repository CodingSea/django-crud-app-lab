from django.urls import path
from . import views

urlpatterns = [
   path("", views.Home, name="Home"),
   path("cat/", views.Cat_List, name="Index"),
   path("cat/new", views.Home, name="Create"),
   path("cat/<int:pk>", views.Cat_Details.as_view(), name="cat-details"),
]
