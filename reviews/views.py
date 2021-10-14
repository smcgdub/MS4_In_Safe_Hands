from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from products.models import Product
from .forms import ProductReviewForm
from .models import ProductReview


@login_required
def add_review(request):
    '''
    View that returns the add a review view
    '''
    review_form = ProductReviewForm()

    # If user is authenticated then review form will show
    if request.user.is_authenticated:
        review_form = ProductReviewForm(initial={
            'reviewer': UserProfile.objects.get(user=request.user)
            })
    else:
    # If user is unregistered then they form will not show
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
                messages.success(request, "Success! Your review has been \
                                           added to our website")
                return redirect(reverse('home'))
            except Exception as e:
                print("Error in try except block: ", e)
                messages.error(request, "There was an error adding your \
                                         review to the site. Please check all \
                                         fields in the form and try again")
                return redirect(reverse('add_review'))
        else:
            print("Error from is form valid else block in ADD_REVIEW")

    template = 'reviews/add_review.html'
    context = {
        'form': review_form,
    }

    return render(request, template, context=context)


@login_required
def edit_review(request, review_id):
    '''
    A view that allows for the editing of a review
    '''
    # Need to test commenting the 2 line of code below out and see if the 
    # edit review function works still. Be sure to check terminal during testing
    # review = get_object_or_404(ProductReview, pk=review_id)
    # review_form = ProductReviewForm(instance=review)

    # product = get_object_or_404(ProductReview, review_id)
    # review_form = ProductReviewForm()

    # If user is authenticated then review form will show
    if request.user.is_authenticated:
        review = get_object_or_404(ProductReview, pk=review_id)
        review_form = ProductReviewForm(instance=review)
        # review_form = ProductReviewForm(initial={
        #     'reviewer': UserProfile.objects.get(user=request.user)
        #     })
    else:
        # If user is unregistered then they will be redirected to the login page
        review_form = ProductReviewForm()

    if request.method == 'POST':
        review_form = ProductReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            print("EDIT REVIEW POST HAS GONE THROUGH IF FORM IS VALID BLOCK")
            messages.success(request, 'Success! The edit you made to your \
                                       review updated')
            return redirect(reverse('home'))
        else:
            print("Error from is form valid else block in EDIT_REVIEW")

    template = 'reviews/edit_review.html'
    context = {
        'form': review_form,
        'review': review,
    }

    return render(request, template, context=context)


@login_required
def delete_review(request):
    '''
    View that returns delete a review
    '''
    return render(request, 'reviews/delete_review.html')
