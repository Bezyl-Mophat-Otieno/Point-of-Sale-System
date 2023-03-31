from django.contrib import admin
from .models import Product,Customer,Order,Sale,Expense
# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Sale)
admin.site.register(Expense)

