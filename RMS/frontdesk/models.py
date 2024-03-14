from django.db import models
from management.models import Table


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact_number = models.IntegerField()
    

class CustomerTable(models.Model):
    customer = models.ForeignKey(Customer,on_delete= models.SET_NULL,null=True)
    table = models.ForeignKey(Table,on_delete=models.SET_NULL,null=True)
