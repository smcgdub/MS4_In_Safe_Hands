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
