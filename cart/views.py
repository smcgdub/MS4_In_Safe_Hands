from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_cart(request):
  # A view that will render the contents of the users shopping cart
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    # Add the item to the shopping cart
 
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # Update cart if item already in cart
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Quantity of {product.name} in cart is now {cart[item_id]} \U0001F44D')
        print("Product quantity updated from product details page")
    else:
        # Add to cart
        cart[item_id] = quantity
        messages.success(request, f'{product.name} added to cart \U0001F44D ')
        print("Product added to cart for first time from product details page")
    
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    # Adjust the number of items in the cart 

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    # If there is more than 1 item in the cart adjust the order
    if quantity > 0:
        cart[item_id] = quantity
        print("Product quantity update from shopping cart")
        messages.success(request, f'Quantity of {product.name} in cart is now {cart[item_id]} \U0001F44D')
    else:
        cart.pop(item_id)
        messages.success(request, f'{product.name} removed from cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    # To remove an item from the shopping cart

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'{product.name} removed from cart \U0001F44D ')
        request.session['cart'] = cart
        print("Product removed from shopping cart from the cart page")
        return redirect(reverse('view_cart'))
    
    except Exception as e:
        messages.error(request, f'Oops! There was an error removing {e} from the cart \U0001F62C ')
        print("Error removing item from cart page")
        return redirect(reverse('view_cart'))
