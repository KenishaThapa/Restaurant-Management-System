from django.contrib import admin
from management.models import User,Table, TableType
from accounting.models import Bill,Payment
from restaurant.models import Menu,Food
from frontdesk.models import Customer,CustomerTable
from ordering.models import Order,Waiter
# Register your models here.
admin.site.register(User)
admin.site.register(Table)
admin.site.register(TableType)
admin.site.register(Bill)
admin.site.register(Payment)
admin.site.register(Menu)
admin.site.register(Food)
admin.site.register(Customer)
admin.site.register(CustomerTable)
admin.site.register(Order)
admin.site.register(Waiter)


