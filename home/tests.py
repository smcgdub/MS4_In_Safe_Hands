from django.test import TestCase


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
