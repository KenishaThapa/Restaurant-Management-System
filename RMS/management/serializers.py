from rest_framework import serializers
from .models import TableType,Table,User
from accounting.models import Bill,Payment
from frontdesk.models import Customer,CustomerTable
from ordering.models import Order,Waiter
from restaurant.models import Menu,Food

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']

class TableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableType
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields ='__all__'
    
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerTable
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

