from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
# Create your views here.

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "You've nothing in your cart at the moment, but here's are all of our products for you to browse \U0001F642")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
      'order_form': order_form,
      'stripe_public_key': 'pk_test_51Jcbx4IXS6q4772pNrmlcRdvJ1UMA2OqeLeitpAoxeql1diJGdEeZBwQ6SW208jmXet2KYFdCUEE0idjMEZoA1P300NmJZiRzG',
      'client_secret': 'Test client secret',
    }

    return render(request, template, context)