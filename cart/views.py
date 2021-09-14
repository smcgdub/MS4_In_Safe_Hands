from django.shortcuts import render

# Create your views here.

def view_cart(request):
  # A view that will render the content sof the users shopping cart

    return render(request, 'cart/cart.html')