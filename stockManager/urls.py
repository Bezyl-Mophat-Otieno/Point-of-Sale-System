from django.urls import path
from . import views

app_name = 'stockManager'

urlpatterns = [

path('addProduct/',views.addProductForm,name='addProduct'),
path('allProducts/',views.allProducts,name='allProducts'),
path('updateProduct/<int:productId>',views.updateProducts,name='updateProduct'),
path('deleteProduct/<int:productId>',views.deleteProduct,name='deleteProduct'),

path('addCustomer/',views.addCustomerForm,name='addCustomer'),
path('allCustomers/',views.allCustomers,name='allCustomers'),
path('updateCustomer/<int:customerId>',views.updateCustomers,name='updateCustomer'),
path('deleteCustomer/<int:customerId>',views.deleteCustomer,name='deleteCustomer'),

path('addOrder/',views.addOrdersForm,name='addOrder'),
path('allOrders/',views.allOrders,name='allOrders'),
path('updateOrder/<int:orderId>',views.updateOrders,name='updateOrder'),
path('deleteOrder/<int:orderId>',views.deleteOrder,name='deleteOrder'),
path('pendingOrders/',views.pendingOrders,name='pendingOrders'),
path('fulfilledOrders/',views.fulfilledOrders,name='fulfilledOrders'),



path('addSale/',views.addSalesForm,name='addSale'),
path('allSales/',views.allSales,name='allSales'),
# path('updateOrder/<int:orderId>',views.updateOrders,name='updateOrder'),
# path('deleteOrder/<int:orderId>',views.deleteOrder,name='deleteOrder'),





]