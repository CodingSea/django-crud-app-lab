from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Cat(models.Model):
    name = models.CharField(120)
    age = models.IntegerField(MinLengthValidator(0))
    color = models.CharField(120)

    class Meta:
        db_table = 'Cat'

