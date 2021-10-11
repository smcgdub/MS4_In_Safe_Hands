from django.db import models
from profiles.models import UserProfile
from products.models import Product


# The review model which allows users to review a product
class ProductReview(models.Model):
    review_title = models.CharField(max_length=90, null=False, blank=False)
    reviewed_product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(UserProfile, null=False, blank=False , on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    # This will correct the spelling in Django admin to the correct plural spelling
    class Meta:
        verbose_name_plural = 'Reviews'

    # To return the title of the review
    def __str__(self):
        return self.review_title