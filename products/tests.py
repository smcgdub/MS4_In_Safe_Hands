from django.test import TestCase
from .models import Product

# Create your tests here.
class TestProducts(TestCase):

    # Test to confirm correct products template page is rendering 
    def test_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    # Test to confirm correct product details template page is rendering 
    def test_product_details_page(self):
        product = Product.objects.create(price='1', name='Test Product') 
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')

    # Test to confirm if a none superuser attempts to access the add product page they will be redirected to the login page 
    def test_adding_product(self):
        response = self.client.post('/products/add/')
        self.assertRedirects(response, '/accounts/login/?next=/products/add/')


    # Test to confirm if a none superuser attempts to access the edit product page they will be redirected to the login page 
    def test_editing_a_product(self):
        product = Product.objects.update(price='1', name='Test product')
        response = self.client.get(f'/products/edit/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/accounts/login/?next=/products/edit/{product.id}/')

