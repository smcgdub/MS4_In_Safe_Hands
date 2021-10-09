# The review model which allows users to review a product
class ProductReview(models.Model):
    review_title = models.CharField(max_length=90, null=False, blank=False)
    reviewed_product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(UserProfile, null=False, blank=False , on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    # To return the title of the review
    def __str__(self):
        return self.review_title


# Forms.py file
class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
      # Fields to dispaly on the contact us form
        fields = ('review_title', 'reviewed_product', 'reviewer', 'review', 'date')
        widgets={'reviewer': HiddenInput(), 'date': HiddenInput()}


    def __init__(self, *args, **kwargs):
        # Placeholders to be added to the checkout fields
        super().__init__(*args, **kwargs)
        placeholders = {
            'review_title': 'Title of your review',
            'reviewed_product': "You're reviewing",
            'reviewer': 'Reviewed by',
            'review': 'Your review here',
            'date': 'Date & Time',
            }

        # Form will auto start on first name
        self.fields['review_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
                # Asterisk will appear on required fields
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # Set placeholders 
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Labels set to false as they are not being used 
            self.fields[field].label = False

# Alternative forms.py option
class ReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        exclude = ('product', 'user', 'date_added')


# If user is authenticated then the priority message will show
if request.user.is_authenticated:
    messages_form = ContactMessagesForm(initial={
        'reviewer': UserProfile.objects.get(user=request.user),
        'reviewed_product': Product.objects.get(pk=product_id)
        })
# If user is unregistered then they form will not show
else:
    messages_form = ContactMessagesForm()

# Views.py 
@login_required
def add_review(request, product_id):
    # A view to allow the user to add a review to a product

    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                messages.success(request, f'Your review of {product.name} has been successfully posted')
                return redirect(reverse('product_details', args=[product.id]))
            else:
                messages.error(
                    request, f'Oops! Something went wrong posting your review. Do you want to try again?')

    template = 'products/product_details.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    # A view to allow the users to edit their review

    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.info(request, f'Success! The edit to your review of {product.name} has now taken effect')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, f'Oops! That review edit failed, please try again')

    else:
        form = ReviewForm(instance=review)

    messages.info(request, f'You are now editing your review of {product.name}')
    template = 'products/product_details.html'
    context = {
        'form': form,
        'review': review,
        'product': product,
        'edit': True,
    }
    return render(request, template, context)

#---------------------------------------------------------------------------------------------------------------------------------

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




#---------------------------------------------------------------------------------------------------------------------------------
# User messages completed 
# class RegisterUserMessages(models.Model):
#     sender = models.ForeignKey(UserProfile.user, on_delete=models.CASCADE)
#     subject = models.CharField(max_length=80, null=False, blank=False)
#     message = models.TextField(max_length=3000, null=False, blank=False)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.subject

#---------------------------------------------------------------------------------------------------------------------------------

# Wishlist 
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



    # This code posts to the django admin ok 
    def contact_us(request):
    # View that returns contact us page
    
    # messages_form = ContactMessagesForm()

    messages_form = ContactMessagesForm(initial={'sender': UserProfile.objects.get(user=request.user)})
    
    if request.method == 'POST':
        messages_form = ContactMessagesForm(request.POST)
        sender = UserProfile.objects.get(user=request.user)
        print(sender)

        if messages_form.is_valid():
            # sender = messages_form.cleaned_data['sender']
            # sender = UserProfile.objects.get(user=request.user)
            # subject = messages_form.cleaned_data['subject']
            # message = messages_form.cleaned_data['message']
            # contact_email = messages_form.cleaned_data['contact_email']
            try:
                print("ENTERING TRY BLOCK")
                # messages_form.save(commit=False)
                # print("SAVING MESSAGE FROM COMMIT FALSE")
                # messages_form.sender = sender
                # print("ADD SENDER TO FORM")
                messages_form.save()
                print("SAVING TO DB")
                messages.success(request, "Your message to us has been successfully sent. We will be in contact as soon as possible")
                return redirect(reverse('home'))
            except Exception as e:
                print("Error in try except block: ", e) # Edited by Jo
                messages.error(request, "There was an error sending your message, please try to send it again")
                return redirect(reverse('contact_us'))
        else:
            print("Error from is form valid else block")
            messages.error(request, "There was an error sending your message, please try to send it again")
            return redirect(reverse('contact_us'))
        
    template = 'contact_us/contact_us.html'
    context = {
        'form': messages_form
    }

    return render(request, template, context=context)



    # Original Code 

# def contact_us(request):
#     # View that returns contact us page
    
#     messages_form = ContactMessagesForm()
#     # profile = UserProfile.objects.get(user=request.user)

#     if request.method == 'POST':
#         messages_form = ContactMessagesForm(ContactMessages)
#         if messages_form.is_valid():
#             messages_form.save()
#             messages.success(request, "Your message to us has been successfully sent")
#             return redirect(reverse('home'))
#         else:
#             messages.error(request, "There was an error sending your message, please try to send it again")
#             return redirect(reverse('home'))
        
#     template = 'contact_us/contact_us.html'
#     context = {
#         'form': messages_form
#     }

#     return render(request, template, context=context)