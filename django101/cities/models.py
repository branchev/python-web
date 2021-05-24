from django.db import models


class Person(models.Model):
    # Class attributes:
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    home_town = models.CharField(max_length=20)

