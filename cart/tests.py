from django.test import TestCase


# Create your tests here.
class TestCart(TestCase):
    '''
    Testing of the cart
    '''
    def test_cart_page(self):
        '''
        Test to confirm correct cart template page is rendering
        '''
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
