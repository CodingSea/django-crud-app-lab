from django import forms
from .models import (Cat, Toy)

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'age', 'color']


class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ['name', 'cat']