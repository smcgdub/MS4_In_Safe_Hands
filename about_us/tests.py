from django.test import TestCase


# Create your tests here.
class TestAboutUs(TestCase):
    '''
    Test to confirm correct about us template page is rendering
    '''
    def test_about_us_page(self):
        '''
        Test to make sure the correct About Us page is rendering to the user
        '''
        response = self.client.get('/about_us/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us/about_us.html')
