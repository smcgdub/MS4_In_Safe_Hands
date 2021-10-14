from django.test import TestCase, Client
from home import apps


# Create your tests here.
class TestHome(TestCase):
    '''
    Tests to be carried out on the homepage
    '''

    def test_home_page(self):
        '''
        Test to confirm correct home template page is rendering
        '''
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')


    def test_sign_up_page(self):
        '''
        Test to confirm if the sign up page is rendering
        '''
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('accounts/signup.html')


    def test_log_in_page(self):
        '''
        Test to confirm if the login page is rendering
        '''
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('accounts/login.html')


    def test_home_configuration(self):
        '''
        Test to make sure the app is configured correctly
        '''
        self.assertEqual(apps.HomeConfig.name, 'home')

