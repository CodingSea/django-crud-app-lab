from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    color = models.CharField(max_length=120)

    class Meta:
        db_table = 'Cat'

