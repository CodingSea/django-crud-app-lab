from django.urls import path
from . import views

urlpatterns = [
   path("", views.Home, name="Home"),
   path("cat/", views.Home, name="Index"),
   path("cat/new", views.Home, name="Create"),
]
