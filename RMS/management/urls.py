from django.urls import path
from management.views import TableTypeView,TableView, UserView, BillView,PaymentView,CustomerView,CustomerTableView,OrderView,WaiterView,MenuView,FoodView
urlpatterns = [
    path('table-type/',TableTypeView.as_view({'get':'list','post':'create'})),
    path('table-type/<int:pk>/',TableTypeView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('table/',TableView.as_view({'get':'list','post':'create'})),
    path('register/',UserView.as_view({'post':'register'}),name='register'),
    path('login/',UserView.as_view({'post':'login'}),name='login'),
    path('bill/',BillView.as_view({'get':'list','put':'update','delete':'destroy'})),
    path('payment/',PaymentView.as_view({'get':'list','put':'update','delete':'destroy'})),
    path('customer/',CustomerView.as_view({'get':'list','put':'update','delete':'destroy'})),
    path('customertable/',CustomerTableView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('order/',OrderView.as_view({'get':'list','put':'update','delete':'destroy'})),
    path('waiter/',WaiterView.as_view({'get':'list','put':'update'})),
    path('menu/',MenuView.as_view({'get':'list','put':'update','delete':'destroy'})),
    path('food/',FoodView.as_view({'get':'list','put':'update','delete':'destroy'})),



]
