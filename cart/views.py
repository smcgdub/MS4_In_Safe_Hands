from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
  # A view that will render the content sof the users shopping cart

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    # Add the quantity of a specific item to the shopping cart

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)