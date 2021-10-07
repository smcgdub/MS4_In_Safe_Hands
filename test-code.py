# The review model which allows users to review a product
class ProductReview(models.Model):
    review_title = models.CharField(max_length=90, null=False, blank=False)
    reviewed_product = models.ForeignKey('Product', null=False, blank=False, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    # To return the title of the review
    def __str__(self):
        return self.review_title

class BillingAddress(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    eircode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Select Country *', null=False, blank=False)

    def __str__(self):
        return self.order_number

class RegisterUserMessages(models.Model):
    sender = models.ForeignKey(UserProfile.user, on_delete=models.CASCADE)
    subject = models.CharField(max_length=80, null=False, blank=False)
    message = models.TextField(max_length=3000, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject




Workflow: 
customer > click on wishlist button > url connected to a view > view will action the function 

> Click on wishlist button
> Check if item already in wish list 
> If yes: remove it from the wish list 
> If no: add it to wishlist 

Effectively we are just creating an if statement 
Button will change display depending on wishlist ("Add to wishlist" if not in the list, "remove from wishlist" if it is in the list)

# in urls
path("wishlist/add_to_wishlist/<int:product_id>/", views.add_to_wishlist, name="user_wishlist")

# Imports
from django.shortcuts import get_object_or_404, redirect, render
from product.models import Product

# User will need to be logged in
@login_required 
def add_to_wishlist(request, product_id):
    
    product = get_object_or_404(Product, pk=product_id)
    redirect_url = request.POST.get('redirect_url')

    if product .users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove()
        messages.success(request, f'{product.name} has been removed to your wishlist \U0001F44D ')       
    else:
        product.users_wishlist.add(request.user)
        messages.success(request, f'{product.name} has been added to your wishlist \U0001F642 ')
    
    return redirect(redirect_url)







def contact_us(request):
    # View that returns contact us page
    messages_form = ContactMessagesForm()

    if request.method == 'POST':
        messages_form = ContactMessagesForm(ContactMessages)
        if messages_form.is_valid():
            messages_form.save()
            messages.success(request, "Your message to us has been successfully sent")
            return redirect(reverse('home'))
    else:
        messages.error(request, "There was an error sending your message, please try to send it again")
        # return redirect(reverse('contact_us'))

    template = 'contact_us/contact_us.html'
    context = {
        'form': messages_form
    }
    return render(request, template, context=context)