from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200,null=True)#null=True means it is nullable i.e not required or rather optional

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class TableType(models.Model):
    name = models.CharField(max_length=200)

class Table(models.Model):
    name = models.CharField(max_length=200) 
    description = models.TextField()
    type = models.ForeignKey(TableType,on_delete = models.SET_NULL,null=True)
    status = models.CharField(max_length=200)



