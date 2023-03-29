from django.db import models

# Create your models here.
# The products we sell at bubble bursts 


class Product(models.Model):
    
    name = models.CharField(max_length=100 , unique=True ,blank=False,null=False)
    quantityProduced = models.IntegerField(blank=False,null=False)
    quantityPacked = models.IntegerField(blank=False,null=False)
    pricePerLitre = models.DecimalField(max_digits=6, decimal_places=2,blank=False,null=False)
    pricePerHalfLitre = models.DecimalField(max_digits=6, decimal_places=2 , blank=False,null=False)
    description = models.TextField(blank=True,null=True)
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        
        return self.name or ''


class Customer (models.Model):
    name = models.CharField(max_length=100 ,blank=True,null=True)
    phone = models.CharField(max_length=100 , blank=True, null=True)
    location = models.CharField(max_length=100 ,blank=True,null=True)
    def __str__(self):
        return self.name or ''
    

# class OrderBalances (models.Manager):

#     def AR(self):
#         return Order.sold_at - Order.amount_paid
    

    
class Order(models.Model):
    
    DELIVERY = (('delivered','delivered'),('delivery pending','delivery pending'))
    PACKAGING = (('500ml bottles','500ml bottles'),('1L bottles','1L bottles'))
    STATUS = (('pending','pending'),('fulfilled','fulfilled'),)
    SP = (('1L @70','1L @70'),('1L @130','1L@ 130'),('500ml @40','500ml @40'), ('500ml @70','500ml@ 70'),)
    customer = models.ForeignKey(Customer,null=True,blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null=True , blank=True , on_delete=models.CASCADE)
    quantity_in_litres = models.DecimalField(max_digits=6, decimal_places=2,blank=False,null=False)
    selling_price  = models.DecimalField(max_digits=6, decimal_places=2,blank=False,null=False)
    sold_at  = models.DecimalField(max_digits=6, decimal_places=2,blank=False,null=False)
    amount_paid  = models.DecimalField(max_digits=6, decimal_places=2,blank=False,null=False)
    delivery = models.CharField(max_length=100,null=True , choices=DELIVERY)
    order_status = models.CharField(max_length=100,null=True , choices=STATUS)
    packaging = models.CharField(max_length=100,null=True , choices=PACKAGING)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    
    
    def __str__(self):
        return self.product.name
    
    
    @property
    def credits (self):
        return self.sold_at - self.amount_paid
    
    def save(self,*args, **kwargs):
        self.balance = self.sold_at - self.amount_paid
        super(Order, self).save(*args, **kwargs)
    

    

    
class Sale(models.Model):
    PACKAGING = (('500ml bottles','500ml bottles'),('1L bottles','1L bottles'))
    customer = models.ForeignKey(Customer,null=True,blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null=True , blank=True , on_delete=models.CASCADE)
    packaging = models.CharField(max_length=100,null=True , choices=PACKAGING)
    pieces = models.IntegerField(default=0 , null=True)
    selling_price  = models.DecimalField(max_digits=6, decimal_places=2,blank=False,null=False)
    date = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.product.name

    
