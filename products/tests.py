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