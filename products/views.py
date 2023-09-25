from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    return render(request, template_name='products/product.html')


def products(request):
    products_data = Product.objects.all().order_by('-price')
    return render(request, template_name='products/products.html', context={'products':products_data})