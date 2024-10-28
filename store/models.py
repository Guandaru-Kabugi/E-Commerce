from typing import Iterable
from django.db import models
import datetime
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()
# Create your models here.

#Product Category
class Category(models.Model):
    name = models.CharField(max_length=60,verbose_name='Category Name')
    
    def __str__(self):
        return self.name
class Product(models.Model):
    product_name = models.CharField(max_length=100,null=False,unique=False,verbose_name='Product Name')
    product_image = models.URLField(max_length=300,verbose_name='Product URL')
    product_description = models.CharField(max_length=300,verbose_name='Product Description')
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Product Category')
    slug_field = models.SlugField(verbose_name='slug_field',max_length=100,unique=True, null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    product_serial_Number = models.CharField(max_length=50,unique=True)
    product_price = models.DecimalField(default=0,max_digits=8,decimal_places=2,verbose_name='Product Price')
    product_quantity = models.PositiveIntegerField(default=0,verbose_name='Product Quantity')
    rating = models.PositiveIntegerField(default=0,verbose_name='Product Rating')
    #check whether a product is on sale/discount
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,max_digits=8,decimal_places=2,verbose_name='Product Sale Price')
    # image = models.ImageField(upload_to='uploads/products/')
    def __str__(self):
        return self.product_name
    def save(self, *args,**kwargs):
        if not self.slug_field:
            self.slug_field = slugify(self.product_name)
        return super().save(*args,**kwargs)
    #customer orders
class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Customer Name')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_ordered = models.DateField(default=datetime.datetime.today)
    address = models.CharField(max_length=100,default='',blank=True)
    status = models.BooleanField(default=False, verbose_name='Status, Whether Delivered or Not')
    
    def __str__(self):
        return f'Ordered: {self.product.product_name} Quantity {self.quantity}'