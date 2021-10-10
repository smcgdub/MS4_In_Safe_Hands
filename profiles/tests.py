from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


# Create your tests here.
class TestProfile(TestCase):
  
    # If the user is not logged in and attempts to access the profile page they will be redirected to the login page
    def test_profile_page(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/profile/')
    
    # def test_login(self):
    #     self.credentials = {
    #                 'username': 'testuser',
    #                 'password': 'secret'}
    #     User.objects.create_user(**self.credentials)

    # def test_login(self):
    #     response = self.client.post('/accounts/login/', self.credentials, follow=True)
    #     self.assertTrue(response.content['user'].is_active)