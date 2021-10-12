from django.test import TestCase

# Create your tests here.
class TestCovidNumbers(TestCase):
    '''
    Tests to be carried out on the covid numbers page
    '''
    def test_covid_numbers_page(self):
        '''
        Test to confirm correct covid numbers template page is rendering
        '''
        response = self.client.get('/covid_numbers/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'covid_numbers/covid_numbers.html')
