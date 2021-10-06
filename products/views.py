from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm
# from .forms import ProductForm, ReviewForm


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


@login_required
def add_product(request):
    # Add a new product to the site 

    # If the user is not a superuser, display error message and redirect them to the homepage 
    if not request.user.is_superuser:
        print("A none superuser is attempting to access a restricted feature add product to store - Products / Views.py / add_product")
        messages.warning(request, 'Sorry, you are not authorized to perform that action')
        return redirect(reverse('home'))

    # If add product form method is POST 
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Add product to store was successful - Products / Views.py / add_product")
            messages.success(request, 'Product has been successfully added to the store')
            # Return user to the products page after they have added the item
            return redirect(reverse('products'))
        # If add product form is invalid
        else:
            messages.warning(request, 'Product add failed! Please recheck all form details are valid')
    # If form isnt a POST form then load a blank form
    else:
        form = ProductForm()
        
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form, 
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    # To edit a product in the store

    # If the user is not a superuser, display error message and redirect them to the homepage 
    if not request.user.is_superuser:
        print("A none superuser is attempting to access a restricted feature edit product in store - Products / Views.py / edit_product")
        messages.warning(request, 'Sorry, you are not authorized to perform that action')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    # If user is posting
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            print("Product was successfully updated - Products / Views.py / edit_product")
            messages.success(request, f'{product.name} has been successfully updated')
            return redirect(reverse('product_details', args=[product.id]))
        # Warning message if updating was unsuccessfull
        else:
            print("There was an error updating the product - Products / Views.py / edit_product")
            messages.warning(request, 'Warning, product update failed. Please check all fields are valid and try again.')
    # Inform user that they are currently editing a product and name that product
    else:
        form = ProductForm(instance=product)
        print("Superuser is currently editing an item - Products / Views.py / edit_product")
        messages.info(request, f'You are currently editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    # Delete the product from the store
    # If the user is not a superuser, display error message and redirect them to the homepage 
    if not request.user.is_superuser:
        print("A none superuser is attempting to access a restricted feature delete product from store - Products / Views.py / delete_product")
        messages.warning(request, 'Sorry, you are not authorized to perform that action')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} has been successfully deleted from the store')
    return redirect(reverse('products'))





# Code for adding a review 
@login_required
def add_review(request, product_id):
    # If add product form method is POST
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Review for {product.name} has been successfully added')
            # Return user to the products page after they have added the item
            return redirect(reverse('product_details'))
        # If add form is invalid
        else:
            messages.warning(request, 'Review failed to post! Please re-check all form details are valid')
    # If form isnt a POST form then load a blank form
    else:
        form = ReviewForm()
        
    form = ReviewForm()
    template = 'products/add_product.html'
    context = {
        'form': form, 
        'product': product,
    }

    return render(request, template, context)