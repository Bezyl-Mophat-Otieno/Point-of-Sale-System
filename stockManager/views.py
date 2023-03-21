from django.shortcuts import render,redirect
from .forms import ProductAddForm,CustomerAddForm,OrderAddForm,SaleAddForm
from django.http import HttpResponseRedirect
from .models import Product,Customer,Order,Sale
from django.contrib import messages
# Create your views here.

# Controller logic for a product 

def addProductForm (request):
    if request.method == 'POST':
        submitted = False
        form =ProductAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Product Added Successfully')
            return HttpResponseRedirect('/stock/allProducts?submitted=True')
        else:
            messages.error(request,'Something went wrong , please try again later')

    else:
        form=ProductAddForm()
        submitted=False
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'stockManager/addProduct.html',{'form':form,'submitted':submitted})

def allProducts(request):
    products = Product.objects.all()
    return render(request,'stockManager/allProducts.html',{'products':products})

def updateProducts(request,productId):
    product = Product.objects.get( pk=productId)
    form = ProductAddForm(request.POST or None,instance=product)
    if form.is_valid():
        form.save()
        messages.success(request,'Product Details Updated Successfully')
        return redirect('/stock/allProducts')

    return render(request , 'stockManager/productUpdate.html',{'product':product,'form':form})

def deleteProduct (request , productId):
    product = Product.objects.get(pk=productId)
    product.delete()
    return redirect ('/stock/allProducts')
    
# Controller logics for a customer 

def addCustomerForm (request):
    if request.method == 'POST':
        submitted = False
        form =CustomerAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Customer Added Successfully')
            return HttpResponseRedirect('/stock/allCustomers?submitted=True')
        
        

    else:
        form=CustomerAddForm()
        submitted=False
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'stockManager/addCustomer.html',{'form':form,'submitted':submitted})



def allCustomers(request):
    customers = Customer.objects.all()
    return render(request,'stockManager/allCustomers.html',{'customers':customers})


def updateCustomers(request,customerId):
    customer = Customer.objects.get( pk=customerId)
    form = CustomerAddForm(request.POST or None,instance=customer)
    if form.is_valid():
        form.save()
        messages.success(request,'Customer Details Updated Successfully')
        return redirect('/stock/allCustomers')

    return render(request , 'stockManager/customerUpdate.html',{'customer':customer,'form':form})

def deleteCustomer (request , customerId):
    customer = Customer.objects.get(pk=customerId)
    customer.delete()
    return redirect ('/stock/allCustomers')
    
# controller logics for the order model


def addOrdersForm (request):
    if request.method == 'POST':
        submitted = False
        form =OrderAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Order Placed Successfully')
            return HttpResponseRedirect('/stock/allOrders?submitted=True')
        
        

    else:
        form=OrderAddForm()
        submitted=False
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'stockManager/addOrders.html',{'form':form,'submitted':submitted})



def allOrders(request):
    orders = Order.objects.all()
    return render(request,'stockManager/allOrders.html',{'orders':orders})


def updateOrders(request,orderId):
    order = Order.objects.get( pk=orderId)
    form = OrderAddForm(request.POST or None,instance=order)
    if form.is_valid():
        form.save()
        messages.success(request,'Order Information Updated Successfully')
        return redirect('/stock/allOrders')

    return render(request , 'stockManager/orderUpdate.html',{'order':order,'form':form})

def deleteOrder (request , orderId):
    order = Order.objects.get(pk=orderId)
    order.delete()
    return redirect ('/stock/allOrders')

# controller logic for the sales controller

def addSalesForm (request):
    if request.method == 'POST':
        submitted = False
        form =SaleAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Sales  Recorded Successfully')
            return HttpResponseRedirect('/stock/allSales?submitted=True')
        
        

    else:
        form=SaleAddForm()
        submitted=False
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'stockManager/addSale.html',{'form':form,'submitted':submitted})



def allSales(request):
    sales = Sale.objects.all()
    return render(request,'stockManager/allSales.html',{'sales':sales})


# def updateSales(request,saleId):
#     sale = Order.objects.get( pk=saleId)
#     form = SalesAddForm(request.POST or None,instance=sale)
#     if form.is_valid():
#         form.save()
#         messages.success(request,'Sales Information Updated Successfully')
#         return redirect('/stock/allSales')

#     return render(request , 'stockManager/saleUpdate.html',{'sale':sale,'form':form})

# def deleteOrder (request , orderId):
#     order = Order.objects.get(pk=orderId)
#     order.delete()
#     return redirect ('/stock/allSales')

