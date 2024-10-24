from django.contrib import admin
from .models import Product,Order,Category
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['product_name','product_image','product_description','product_category','slug_field','date_added','date_updated','product_serial_Number','product_price','product_quantity','rating']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['customer', 'product', 'quantity', 'date_ordered', 'address', 'status']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =['name']