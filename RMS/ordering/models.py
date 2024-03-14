from django.db import models
from frontdesk.models import Customer
from management.models import Table
from restaurant.models import Food

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    table = models.ForeignKey(Table,on_delete=models.SET_NULL,null=True)
    food = models.ForeignKey(Food,on_delete=models.SET_NULL,null=True)
    description = models.TextField() #quantity and ingredients

class Waiter(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)