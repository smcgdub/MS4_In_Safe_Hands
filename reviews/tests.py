from django.test import TestCase

# Create your tests here.
class Reviews(TestCase):

    # If the user has nothing in the shopping cart and attempts to access the checkout page they will be redirected to the products page
    def test_review_page(self):
        response = self.client.get('/reviews/add_review')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/reviews/add_review')