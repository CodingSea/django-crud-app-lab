from django.shortcuts import render, redirect
from .models import Cat
from .forms import CatForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):

    return render(request, "home.html")

@login_required
def cat_list(request):
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

def cat_update_with_form(request, pk):
    cat = Cat.objects.get(id=pk)

    if request.method == "POST":
        form = CatForm(request.POST, instance=cat)

        if form.is_valid():
            cat = form.save()
            return redirect("Index")
    else:
        form = CatForm(instance=cat)
    
    return render(request, "cat-form.html", {"form": form, "mode": "Update"})

def cat_delete(request, pk):
    Cat.objects.get(id=pk).delete()
    return redirect("Index")

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpViews(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/sign-up.html"
    