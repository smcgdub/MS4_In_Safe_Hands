from django.shortcuts import render
from .models import Product


# Create your views here.

def all_products(request):
# View to return all of the products

    products = Product.objects.all()

    context = {'products': products,}

    return render(request, 'products/products.html', context)