from django.urls import path
from . import views

app_name = 'stockManager'

urlpatterns = [
    #Authentication patterns
path('',views.loginPage,name='login'),
path('logout',views.logoutUser,name='logout'),
path('register/',views.register,name='register'),
    #Product patterns
path('addProduct/',views.addProductForm,name='addProduct'),
path('allProducts/',views.allProducts,name='allProducts'),
path('updateProduct/<int:productId>',views.updateProducts,name='updateProduct'),
path('deleteProduct/<int:productId>',views.deleteProduct,name='deleteProduct'),
    #Customer Patters 
path('addCustomer/',views.addCustomerForm,name='addCustomer'),
path('allCustomers/',views.allCustomers,name='allCustomers'),
path('updateCustomer/<int:customerId>',views.updateCustomer,name='updateCustomer'),
path('deleteCustomer/<int:customerId>',views.deleteCustomer,name='deleteCustomer'),

path('addExpense/',views.expenseAddForm,name='addExpense'),
path('allExpenses/',views.allExpenses,name='allExpenses'),
path('updateExpense/<int:expenseId>',views.updateExpense,name='updateExpense'),
path('deleteExpense/<int:expenseId>',views.deleteCustomer,name='deleteExpense'),

    #Order patterns 
path('addOrder/',views.addOrdersForm,name='addOrder'),
path('allOrders/',views.allOrders,name='allOrders'),
path('updateOrder/<int:orderId>',views.updateOrders,name='updateOrder'),
path('deleteOrder/<int:orderId>',views.deleteOrder,name='deleteOrder'),
path('pendingOrders/',views.pendingOrders,name='pendingOrders'),
path('fulfilledOrders/',views.fulfilledOrders,name='fulfilledOrders'),


    #sale patterrns
path('addSale/',views.addSalesForm,name='addSale'),
path('allSales/',views.allSales,name='allSales'),
path('outstandingInvoices/',views.outstandingInvoices,name='outstandingInvoices'),
# path('updateOrder/<int:orderId>',views.updateOrders,name='updateOrder'),
# path('deleteOrder/<int:orderId>',views.deleteOrder,name='deleteOrder'),





]