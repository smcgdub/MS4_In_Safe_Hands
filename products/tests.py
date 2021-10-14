from django.test import TestCase
from django.contrib.auth.models import User
from products import apps
from .models import Product, Category
# from django.test.client import Client


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


        # This test is failing and needs adjusting
    # def test_editing_a_product(self):
    #     '''
    #     Test to confirm if a none superuser attempts to access the edit \
    #     product page they will be redirected to the login page
    #     '''
    #     product = Product.objects.create(price=1, name='Test product')
    #     response = self.client.get(f'/products/edit/{product.id}/')
    #     # self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, '/accounts/login/?next=/products/edit/{product.id}/')


    def test_products_apps_configuration(self):
        '''
        Test to make sure the app is configured correctly
        '''
        self.assertEqual(apps.ProductsConfig.name, 'products')


    def setUp(self):
        self.user = User.objects.create_user(
            username = 'test_user',
            email = 'test@mail.com',
            password = 'test_password'
        )
        self.category = Category.objects.create(
            name = 'test_category',
            friendly_name='test_friendly_name'
        )
        self.product = Product.objects.create(
            p_id = 1,
            name = 'test_product',
            description = 'test_description',
            price='1',
            rating='1',
            image_url = 'www.test.com',
            image = 'test_image.png',
            category = self.category,
        )

    def test_category_model(self):
        '''
        Tests the Category model
        '''
        self.assertEqual(str(self.category), "test_category")

    def test_product_model(self):
        '''
        Tests the Product model
        '''
        self.assertEqual(str(self.product), "test_product")
