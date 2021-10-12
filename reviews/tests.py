from django.test import TestCase

# Create your tests here.
class Reviews(TestCase):
    '''
    Tests for the reviews
    '''
    def test_review_page(self):
        '''
        Confirms the reviews template page will load
        '''
        response = self.client.get('/reviews/add_review')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/reviews/add_review')
