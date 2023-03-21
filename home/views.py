from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from stockManager.models import Product , Customer , Order , Sale
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render



def index(request):
    orderList  = Order.objects.all();
    pendingOrders = orderList.filter(status='pending').count()
    fulfilledOrders = orderList.filter(status='fulfilled').count()
    saleList  = Sale.objects.all();
    sales = saleList.count()
    productList  = Product.objects.all();
    products = productList.count()
    customerList  = Customer.objects.all();
    customers = customerList.count()

    context = { 'pending':pendingOrders , 'fulfilled':fulfilledOrders, 'sales':sales , 'products':products , 'customers':customers ,'saleList':saleList }
    return render(request, 'home/home.html',context)