from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import F , Sum
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
    # Calculatiing the revenue accrued by the sales 
    revenue = Sale.objects.aggregate(total=Sum(F('selling_price')*F('pieces')))['total']
    # render top sales in the home page 
    topSales = Sale.objects.filter(pieces__gte=10).order_by('-pieces')[:5]
    #render the list of products that we currently have in stock 
    products = Product.objects.all().count()

    

    

    context = { 'pending':pendingOrders , 'fulfilled':fulfilledOrders, 'sales':sales , 'products':products , 'customers':customers ,'saleList':saleList , 'revenue':revenue , 'topSales':topSales , 'products':products }
    return render(request, 'home/home.html',context)