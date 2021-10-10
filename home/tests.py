from django.test import TestCase

# Create your tests here.
class TestHome(TestCase):
  
    # Test to confirm correct home template page is rendering 
    def test_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')