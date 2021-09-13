from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
# View to return all of the products, search and sort queries also included

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # For when users click on a specific category of items in the drop down menu 
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey) 

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    # Search function if the user has submitted a search term/word 
        if 'q' in request.GET:
            query = request.GET['q']
            # If the user doesn't enter anything in the search box and presses search the site will load all the products
            if not query:
                messages.error(request, "You haven't entered anything to search for!")
                return redirect(reverse('products'))

            # Q allows to search for product by a product name or by a word in the description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        # 'categories': categories
        }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
# View to return details on individual products

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
        # 'categories': categories
        }
    return render(request, 'products/product_details.html', context)