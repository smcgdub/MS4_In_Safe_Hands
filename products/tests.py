from django.test import TestCase
from .models import Product

# Create your tests here.
class TestProducts(TestCase):
    '''
    Tests to be run on the product and product details pages
    '''

    def test_products_page(self):
        '''
        Test to confirm correct products template page is rendering
        '''
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')


    def test_product_details_page(self):
        '''
        Test to confirm correct product details template page is rendering
        '''
        product = Product.objects.create(price='1', name='Test Product')
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')


    def test_adding_product(self):
        '''
        Test to confirm if a none superuser attempts to access the add \
        product page they will be redirected to the login page
        '''
        response = self.client.post('/products/add/')
        self.assertRedirects(response, '/accounts/login/?next=/products/add/')


    def test_editing_a_product(self):
        '''
        Test to confirm if a none superuser attempts to access the edit \
        product page they will be redirected to the login page
        '''
        # This test is failing and needs adjusting
        product = Product.objects.create(price='1', name='Test product')
        response = self.client.get(f'/products/edit/{product.id}')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/products/edit/{product.id}/')

