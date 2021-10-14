from django.test import TestCase
from reviews import apps
# from django.contrib.auth.models import User
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
        self.assertRedirects(response, '/accounts/login/?next=/reviews/add_review/')


    def test_reviews_apps_configuration(self):
        '''
        Test to make sure the app is configured correctly
        '''
        self.assertEqual(apps.ReviewsConfig.name, 'reviews')
