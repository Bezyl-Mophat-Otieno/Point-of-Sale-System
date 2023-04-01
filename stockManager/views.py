from django.shortcuts import render,redirect
from .forms import ProductAddForm,CustomerAddForm,OrderAddForm,SaleAddForm,userRegisterForm,ExpenseAddForm
from django.http import HttpResponseRedirect
from .models import Product,Customer,Order,Expense
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# Controller logic for a product 
@login_required(login_url='/')
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
@login_required(login_url='/')
def allProducts(request):
    products = Product.objects.all()
    return render(request,'stockManager/allProducts.html',{'products':products})


@login_required(login_url='/')
def updateProducts(request,productId):
    product = Product.objects.get( pk=productId)
    form = ProductAddForm(request.POST or None,instance=product)
    if form.is_valid():
        form.save()
        messages.success(request,'Product Details Updated Successfully')
        return redirect('/stock/allProducts')

    return render(request , 'stockManager/productUpdate.html',{'product':product,'form':form})


@login_required(login_url='/')
def deleteProduct (request , productId):
    product = Product.objects.get(pk=productId)
    product.delete()
    return redirect ('/stock/allProducts')
    
# Controller logics for a customer 

@login_required(login_url='/')
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



@login_required(login_url='/')
def allCustomers(request):
    customers = Customer.objects.all()
    return render(request,'stockManager/allCustomers.html',{'customers':customers})


@login_required(login_url='/')
def updateCustomer(request,customerId):
    customer = Customer.objects.get( pk=customerId)
    form = CustomerAddForm(request.POST or None,instance=customer)
    if form.is_valid():
        form.save()
        messages.success(request,'Customer Details  Updated Successfully')
        return redirect('/stock/allCustomers')

    return render(request , 'stockManager/customerUpdate.html',{'customer':customer,'form':form})

def deleteCustomer (request , customerId):
    customer = Customer.objects.get(pk=customerId)
    customer.delete()
    return redirect ('/stock/allCustomers')
    



# Controller logics for expenses 

@login_required(login_url='/')
def expenseAddForm (request):
    if request.method == 'POST':
        submitted = False
        form =ExpenseAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Expense Recorded Successfully')
            return HttpResponseRedirect('/stock/allExpenses?submitted=True')
        
        

    else:
        form=ExpenseAddForm()
        submitted=False
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'stockManager/addExpense.html',{'form':form,'submitted':submitted})



@login_required(login_url='/')
def allExpenses(request):
    expenses = Expense.objects.all()
    return render(request,'stockManager/allExpenses.html',{'expenses':expenses})




@login_required(login_url='/')
def updateExpense(request,expenseId):
    expense = Expense.objects.get( pk=expenseId)
    form = ExpenseAddForm(request.POST or None,instance=expense)
    if form.is_valid():
        form.save()
        messages.success(request,'Expenses Updated Successfully')
        return redirect('/stock/allExpenses')

    return render(request , 'stockManager/expenseUpdate.html',{'expense':expense,'form':form})

def deleteExpense (request , expenseId):
    expense = Expense.objects.get(pk=expenseId)
    expense.delete()
    return redirect ('/stock/allExpenses')
    


# controller logics for the order model
@login_required(login_url='/')
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


@login_required(login_url='/')
def allOrders(request):
    orders = Order.objects.all()
    return render(request,'stockManager/allOrders.html',{ 'orders':orders })


@login_required(login_url='/')
def pendingOrders(request):
    orders = Order.objects.filter(order_status='pending')
    return render(request,'stockManager/allOrders.html',{'orders':orders})


@login_required(login_url='/')
def fulfilledOrders(request):
    orders = Order.objects.filter(order_status='fulfilled')
    return render(request,'stockManager/allOrders.html',{'orders':orders})


@login_required(login_url='/')
def updateOrders(request,orderId):
    order = Order.objects.get( pk=orderId)
    form = OrderAddForm(request.POST or None,instance=order)
    if form.is_valid():
        form.save()
        messages.success(request,'Order Information Updated Successfully')
        return redirect('/stock/allOrders')

    return render(request , 'stockManager/orderUpdate.html',{'order':order,'form':form})


@login_required(login_url='/')
def deleteOrder (request , orderId):
    order = Order.objects.get(pk=orderId)
    order.delete()
    return redirect ('/stock/allOrders')


@login_required(login_url='/')
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



@login_required(login_url='/')
def allSales(request):
    sales = Order.objects.filter (sold_at__gt=0 )
    
    return render(request,'stockManager/allSales.html',{'sales':sales})



@login_required(login_url='/')
def outstandingInvoices(request):
    #getting the list of sales where customers still have a balance due.
    sales = Order.objects.filter (balance__gt=0 )
    
    return render(request,'stockManager/allSales.html',{'sales':sales})




#contains logic for authentication
def loginPage (request):
    if request.user.is_authenticated:
       return redirect('home/dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'Log-In Successful')
                return redirect('/home/dashboard')
            else:
                messages.info(request,'Username or Password is incorrect')
            
        context = {}    
        return render(request,'stockManager/login.html' , context)


#logout logic
def logoutUser (request):
    logout(request)
    messages.success(request,'Log-Out Successful')
    return redirect('/')

@login_required(login_url='/')
def register (request):
    if request.user.is_authenticated:
       return redirect('home/dashboard')
    else:
        form = userRegisterForm()
        if request.method == 'POST':
            form = userRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account Created Successfully For ' + user )
                return redirect('/')
            else:
                print(form.errors)
        return render(request,'stockManager/register.html' , {'form':form})

