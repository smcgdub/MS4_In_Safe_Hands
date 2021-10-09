from django.test import TestCase

# Create your tests here.
class TestAboutUs(TestCase):
  
    # Test to confirm correct cart template page is rendering 
    def test_covid_numbers_page(self):
        response = self.client.get('/covid_numbers/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'covid_numbers/covid_numbers.html')