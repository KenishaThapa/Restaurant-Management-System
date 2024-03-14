from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from management.models import TableType,Table, User
from accounting.models import Bill,Payment
from frontdesk.models import Customer,CustomerTable
from ordering.models import Order,Waiter
from restaurant.models import Menu,Food
from .serializers import TableTypeSerializer,TableSerializer,UserSerializer,BillSerializer,PaymentSerializer,CustomerSerializer,CustomerTableSerializer,OrderSerializer,WaiterSerializer,MenuSerializer,FoodSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate #to check if data exists or not when logging in
from django.contrib.auth.hashers import make_password #to encrypt password
from rest_framework.authtoken.models import Token #for generating token
from rest_framework.permissions import AllowAny

# Create your views here.
class MenuView(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class FoodView(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class WaiterView(ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer

class CustomerView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerTableView(ModelViewSet):
    queryset = CustomerTable.objects.all()
    serializer_class = CustomerTableSerializer


class BillView(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class PaymentView(ModelViewSet):
    queryset = Payment.objects.all
    serializer_class = PaymentSerializer

class TableTypeView(ModelViewSet):
    queryset = TableType.objects.all()
    serializer_class = TableTypeSerializer

class TableView(ModelViewSet):
    query_set = Table.objects.all()
    serializer_class = TableSerializer
    
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



    def register(self,request):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                password = request.data.get('password')
                hash_password = make_password(password)
                a = serializer.save(password=hash_password)
                a.password = hash_password
                a.save() #it will return the given data
                return Response('User created!')
            else:
                return Response(serializer.errors)
        
    def login(self,request):
        email = request.data.get('email')#asking email and password
        password = request.data.get('password')

        user = authenticate(username=email,password=password)#if username matches previously stored,it will return the data or else it wont.
        if user == None: #if data doesnt matches the stored, then login unsucessful
            return Response('Invalid credentials!')
        else:
            token,_ = Token.objects.get_or_create(user=user)
            return Response(token.key)
     
 
    

    