from django.shortcuts import render
from .models import Cat

# Create your views here.

def Home(request):

    return render(request, "home.html")

def Cat_List(request):
    cats = Cat.objects.all()
    return render(request, "cat-list.html", {"cats": cats})



from django.views.generic import (CreateView, DetailView)

class Cat_Details(DetailView):
    model = Cat
    template_name = "cat-details.html"
    context_object_name = "cat"