from django import forms
from django.forms import ModelForm
from .models import Product, Customer,Order,Sale,Expense
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm









class ProductAddForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantityProduced', 'quantityPacked', 'pricePerLitre', 'pricePerHalfLitre','description',]

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'quantityProduced':forms.NumberInput(attrs={'class':'form-control'}),
            'quantityPacked':forms.NumberInput(attrs={'class':'form-control'}),
            'pricePerLitre':forms.TextInput(attrs={'class':'form-control'}),
            'pricePerHalfLitre':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }

class CustomerAddForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone','location',]

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class OrderAddForm(ModelForm):
    class Meta:
        model = Order
        fields =['customer','product','quantity_in_litres','selling_price','sold_at','amount_paid','packaging','delivery','order_status',]


        widgets = {
            'customer':forms.Select(attrs={'class':'form-control'}),
            'product':forms.Select(attrs={'class':'form-control'}),
            'quantity_in_litres':forms.NumberInput(attrs={'class':'form-control'}),
            'selling_price':forms.NumberInput(attrs={'class':'form-control'}),
            'sold_at':forms.NumberInput(attrs={'class':'form-control'}),
            'amount_paid':forms.NumberInput(attrs={'class':'form-control'}),
            'packaging':forms.Select(attrs={'class':'form-control'}),
            'delivery':forms.Select(attrs={'class':'form-control'}),
            'order_status':forms.Select(attrs={'class':'form-control'}),
        }


class SaleAddForm(ModelForm):
      class Meta:
        model = Sale
        fields =['customer','product','pieces','selling_price','packaging',]



        widgets = {
            'customer':forms.Select(attrs={'class':'form-control'}),
            'product':forms.Select(attrs={'class':'form-control'}),
            'packaging':forms.Select(attrs={'class':'form-control'}),
            'pieces':forms.NumberInput(attrs={'class':'form-control'}),
            'selling_price':forms.TextInput(attrs={'class':'form-control'}),
        }

class userRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields =['email','username','password1','password2',]


        widgets = {
            'email':forms.Select(attrs={'class':'form-control'}),
            'username':forms.Select(attrs={'class':'form-control'}),
            'password1':forms.NumberInput(attrs={'class':'form-control'}),
            'password2':forms.Select(attrs={'class':'form-control'}),
        }


class ExpenseAddForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_tittle','amount_spent',]

        widgets = {
            'expense_tittle':forms.TextInput(attrs={'class':'form-control'}),
            'amount_spent':forms.NumberInput(attrs={'class':'form-control'}),
        }