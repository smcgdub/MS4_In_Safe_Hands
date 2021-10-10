from django.test import TestCase

# Create your tests here.
class TestCheckout(TestCase):

    # If the user has nothing in the shopping cart and attempts to access the checkout page they will be redirected to the products page
    def test_checkout_page(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')