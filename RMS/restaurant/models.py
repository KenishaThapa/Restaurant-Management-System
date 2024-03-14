from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)

class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
