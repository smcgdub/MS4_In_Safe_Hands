from django.test import TestCase

# Create your tests here.
class TestAboutUs(TestCase):

    # Test is failing as no item is in cart on this
    # Test to confirm correct about us template page is rendering 
    def test_checkout_page(self):
        response = self.client.get('/checkout/')
        self.assertNotEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')