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

    # 
    if request.GET:
        # If user is looking to sort the results 
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

        # If user is searching via category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Search function if the user has submitted a search term/word 
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
            # If the user doesn't enter anything in the search box and presses search the site will load the all products page with the mesage below
                messages.info(request, "You didn't enter anything to search for....but here's all our products \U0001F642 ")
                return redirect(reverse('products'))

            # Q allows to search for product by a product name or by a word in the description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    # Return sorting to the template 
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
# View to return details on individual products

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
        }
    return render(request, 'products/product_details.html', context)