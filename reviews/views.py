from django.shortcuts import render


# Create your views here.
def add_review(request):
    # View that returns add a review
    return render(request, 'reviews/add_review.html')


def edit_review(request):
    # View that returns edits a review
    return render(request, 'reviews/edit_review.html')


def delete_review(request):
    # View that returns delete a review
    return render(request, 'reviews/delete_review.html')