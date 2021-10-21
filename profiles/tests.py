from django.test import TestCase
# from django.contrib.auth.models import User
from profiles import apps
# from .models import UserProfile
from .forms import UserProfileForm


# Create your tests here.
class TestProfile(TestCase):
    '''
    Tests to run on the user profile page
    '''
    def test_profile_page(self):
        '''
        If the user is not logged in and attempts to access the profile page \
        they will be redirected to the login page
        '''
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/profile/')

    def test_profiles_apps_configuration(self):
        '''
        Test to make sure the app is configured correctly
        '''
        self.assertEqual(apps.ProfilesConfig.name, 'profiles')

    def test_user_profile_form_is_valid(self):
        '''
        A test to confirm the fields that are required for the form to \
        be valid. Only the user form is a required field.
        '''
        form = UserProfileForm({
                               'user': 'user',
                               'default_email': '',
                               'default_phone_number': '',
                               'default_street_address1': '',
                               'default_street_address2': '',
                               'default_town_or_city': '',
                               'default_county': '',
                               'default_eircode': '',
                               'default_country': '',
                               })
        self.assertTrue(form.is_valid())

    # def test_login(self):
    #     self.credentials = {
    #                 'username': 'testuser',
    #                 'password': 'secret'}
    #     User.objects.create_user(**self.credentials)

    # def test_login(self):
    #     response = self.client.post(
    #     '/accounts/login/', self.credentials, follow=True)
    #     self.assertTrue(response.content['user'].is_active)
