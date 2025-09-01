from django.shortcuts import render, redirect
from .models import Cat
from .forms import CatForm
from django.urls import reverse_lazy

# Create your views here.

def Home(request):

    return render(request, "home.html")

def Cat_List(request):
    cats = Cat.objects.all()
    return render(request, "cat-list.html", {"cats": cats})



from django.views.generic import (CreateView, DetailView)

class Cat_Create(CreateView):
    model = Cat
    template_name = "cat-form.html"
    success_url = reverse_lazy("Index")

class Cat_Details(DetailView):
    model = Cat
    template_name = "cat-details.html"
    context_object_name = "cat"


def cat_create_with_form(request):
    if request.method == "POST":
        form = CatForm(request.POST)

        if form.is_valid():
            cat = form.save()
            return redirect("Index")

    form = CatForm()
    return render(request, "cat-form.html", {"form": form})