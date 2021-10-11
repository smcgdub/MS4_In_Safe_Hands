from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductReviewForm
from .models import ProductReview
from profiles.models import UserProfile
from products.models import Product



@login_required
def add_review(request):
    # View that returns add a review
    review_form = ProductReviewForm()

    # If user is authenticated then review form will show 
    if request.user.is_authenticated:
        review_form = ProductReviewForm(initial={'reviewer': UserProfile.objects.get(user=request.user)})
    # If user is unregistered then they form will not show
    else:
        review_form = ProductReviewForm()
    
    if request.method == 'POST':
        review_form = ProductReviewForm(request.POST)
        sender = UserProfile.objects.get(user=request.user)
        print(sender)

        if review_form.is_valid():
            try:
                print("ENTERING TRY BLOCK")
                review_form.save()
                print("SAVING TO DB")
                messages.success(request, f"Success! Your review has been added to our website")
                return redirect(reverse('home'))
            except Exception as e:
                print("Error in try except block: ", e)
                messages.error(request, f"There was an error adding your review to the site. Please check all fields in the form and try again")
                return redirect(reverse('add_review'))
        else:
            print("Error from is form valid else block in ADD_REVIEW")

    template = 'reviews/add_review.html'
    context = {
        'form': review_form,
    }

    return render(request, template, context=context)


@login_required
def edit_review(request):
    # View that returns edits a review
    return render(request, 'reviews/edit_review.html')


@login_required
def delete_review(request):
    # View that returns delete a review
    return render(request, 'reviews/delete_review.html')