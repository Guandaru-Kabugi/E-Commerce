from django.shortcuts import render
from .models import Product
# Create your views here.
def homepage(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request,'index.html',context)
def about(request):
    context = {}
    return render(request,'about.html',context)
def product(request,slug):
    product = Product.objects.get(slug_field=slug)
    context = {"products":product}
    return render(request,'product.html',context)