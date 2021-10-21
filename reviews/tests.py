from django.test import TestCase
from reviews import apps
from django.contrib.auth.models import User
from .forms import ProductReviewForm
# from django.test import Client


# Create your tests here.
class Reviews(TestCase):
    '''
    Tests for the reviews page
    '''
    def test_review_page(self):
        '''
        Confirms the redirect if a none registered user tries to access the \
        reviews page via typing the path in the browser
        '''
        response = self.client.get('/reviews/add_review/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/reviews/add_review/')

    def test_reviews_apps_configuration(self):
        '''
        Test to make sure the app is configured correctly
        '''
        self.assertEqual(apps.ReviewsConfig.name, 'reviews')

    def setUp(self):
        self.credentials = {
            'username': 'test_user',
            'password': 'password',
        }
        User.objects.create_user(**self.credentials)

    def test_review_form_all_fields_completed(self):
        '''
        A test to confirm that the form is valid if all the fields are \
        completed
        '''
        # response = self.client.post('/login/', self.credentials, follow=True)
        # self.assertTrue(response.context['user'].is_authenticated)

        form = ProductReviewForm({
                                 'review_title': 'review_title',
                                 'reviewed_product': 'reviewed_product',
                                 'reviewer': 'reviewer',
                                 'review': 'review',
                                 'date': 'date',
                                 })
        self.assertTrue(form.is_valid())

    def test_review_form_required_field_date(self):
        '''
        A test to confirm that date field is required on the product \
        review form.
        '''
        form = ProductReviewForm({
                                 'review_title': 'review_title',
                                 'reviewed_product': 'reviewed_product',
                                 'reviewer': 'reviewer',
                                 'review': 'review',
                                 'date': ''
                                 })
        self.assertFalse(form.is_valid())

    def test_review_form_required_field_review(self):
        '''
        A test to confirm that review field is required on the product \
        review form.
        '''
        form = ProductReviewForm({
                                 'review_title': 'review_title',
                                 'reviewed_product': 'reviewed_product',
                                 'reviewer': 'reviewer',
                                 'review': '',
                                 'date': 'date'
                                 })
        self.assertFalse(form.is_valid())

    def test_review_form_required_field_reviewer(self):
        '''
        A test to confirm that reviewer field is required on the product \
        review form.
        '''
        form = ProductReviewForm({
                                 'review_title': 'review_title',
                                 'reviewed_product': 'reviewed_product',
                                 'reviewer': '',
                                 'review': 'review',
                                 'date': 'date'
                                 })
        self.assertFalse(form.is_valid())

    def test_review_form_required_field_reviewed_product(self):
        '''
        A test to confirm that reviewed product field is required on the \
        product review form.
        '''
        form = ProductReviewForm({
                                 'review_title': 'review_title',
                                 'reviewed_product': '',
                                 'reviewer': 'reviewer',
                                 'review': 'review',
                                 'date': 'date'
                                 })
        self.assertFalse(form.is_valid())

    def test_review_form_required_field_review_title(self):
        '''
        A test to confirm that review title field is required on the product \
        review form.
        '''
        form = ProductReviewForm({
                                 'review_title': '',
                                 'reviewed_product': 'reviewed_product',
                                 'reviewer': 'reviewer',
                                 'review': 'review',
                                 'date': 'date'
                                 })
        self.assertFalse(form.is_valid())
