from django.test import TestCase



class TestCheckout(TestCase):
    '''
    Tests for the checkout page
    '''
    def test_checkout_page(self):
        '''
        If the user has nothing in the shopping cart and attempts to access \
        the checkout page they will be redirected to the products page
        '''
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')
