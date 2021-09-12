from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
# View to return all of the products

    products = Product.objects.all()

    # Search function if the user has submitted a search term/word 
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            # If the user doesn't enter anything in the search box and presses search the homepage will reload
            if not query:
                messages.error(request, "You haven't entered anything to search for!")
                return redirect(reverse('home'))

            # Q allows to search for product by a product name or by a word in the description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {'products': products,}
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
# View to return details on individual products

    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product,}
    return render(request, 'products/product_details.html', context)