from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import F , Sum
from stockManager.models import Product , Customer , Order , Expense
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url=('/'))
def index(request):
    orderList  = Order.objects.all();
    pendingOrders = orderList.filter(order_status='pending').count()
    fullFilledOrdersCount = orderList.filter(order_status='fulfilled').count()
    productList  = Product.objects.all();
    products = productList.count()
    customerList  = Customer.objects.all();
    #Display the list of expenses incurred
    expenses = Expense.objects.all()
    totalExpenses = expenses.aggregate(total=Sum(F('amount_spent')))['total'] 
    customers = customerList.count()
    # Calculatiing the revenue accrued by the sales 
    sales = Order.objects.filter (sold_at__gt=0 )
    revenue = sales.aggregate(total=Sum(F('amount_paid')))['total'] - totalExpenses
    accountsRecievable = sales.aggregate(total=Sum(F('balance')))['total']
    #Counting the total number of sales made 
    salesCount = sales.count();
    # render top sales in the home page 
    topSales = sales.filter(quantity_in_litres__gte=5).order_by('-quantity_in_litres')[:5]
    #render the list of products that we currently have in stock 
    products = Product.objects.all().count()


    context = { 'pending':pendingOrders , 'fulfilled':fullFilledOrdersCount, 'salesCount':salesCount , 'products':products , 'customers':customers , 'revenue':revenue , 'topSales':topSales , 'products':products , 'sales':sales , 'accountsRecievable':accountsRecievable, 'totalExpenses':totalExpenses }
    return render(request, 'home/home.html',context)

def aboutPage(request):
    return render(request, 'home/about.html')