from django.urls import path
from . import views

urlpatterns = [
   path("", views.home, name="Home"),
   path("cat/", views.cat_list, name="Index"),
   path("cat/new", views.cat_create_with_form, name="Create"),
   path("cat/<int:pk>", views.Cat_Details.as_view(), name="cat-details"),
   path("cat/<int:pk>/edit", views.cat_update_with_form, name="cat-update"),
   path("cat/<int:pk>/delete", views.cat_delete, name="cat-delete"),
]
