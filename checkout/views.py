from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .models import Order, OrderLineItem
from cart.contexts import cart_contents
from products.models import Product
from .forms import OrderForm

import stripe
# Create your views here.

def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # If checkout form is a POST form
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        # Data from the checkout form 
        form_data = {
            'first_name': request.POST['first_name'], 
            'last_name': request.POST['last_name'], 
            'email': request.POST['email'], 
            'phone_number': request.POST['phone_number'], 
            'street_address1': request.POST['street_address1'], 
            'street_address2': request.POST['street_address2'], 
            'town_or_city': request.POST['town_or_city'], 
            'county': request.POST['county'], 
            'eircode': request.POST['eircode'], 
            'country': request.POST['country'], 
        }
        order_form = OrderForm(form_data)
        # If order is valid
        if order_form.is_valid():
            order = order_form.save()
            # Loop through items in cart 
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                # If there is an error with the users cart the below message will be generated
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found in our database. Please contact us for assistance."
                        )
                    )
                    # Order is deleted and user is redirected back to the shopping cart
                    order.delete()
                    return redirect(reverse('view_cart'))
            # If form posted successfully redirect to checkout success page
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        # Error message if form is filled out incorrect 
        else:
            messages.error(request, 'There was an error with your form. Please recheck all the details entered.')
    # If shopping cart is empty the error message below will be generated
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "You've nothing in your cart at the moment, but here's are all of our products for you to browse \U0001F642")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        # Stripe intent referenced in docs: https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements#web-create-payment-intent
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            # Verify your integration in this guide by including this parameter
            # metadata={'integration_check': 'accept_a_payment'},
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing!')

    template = 'checkout/checkout.html'
    context = {
      'order_form': order_form,
      'stripe_public_key': stripe_public_key,
      'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    # If checkout has been successful
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order has been successfully placed \
        Your order number is {order_number}. A confirmation email \
        will be sent to {order.email}')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)