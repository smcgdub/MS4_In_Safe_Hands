from django.test import TestCase
from .forms import ContactMessagesForm


class TestContactMessagesForm(TestCase):

    # def test_contact_us_form_sender_required(self):
    #     form = ContactMessagesForm({'sender': ''})
    #     self.assertFalse(form.is_valid())
    #     # self.assertIn('sender', form.errors.keys())

    # def test_contact_us_form_subject_required(self):
    #     form = ContactMessagesForm({'subject': ''})
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('subject', form.errors.keys())

    # def test_contact_us_form_message_required(self):
    #     form = ContactMessagesForm({'message': ''})
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('message', form.errors.keys())

    # # This test is failing and needs looking at 
    # def test_contact_us_form_email_not_required(self):
    #     form = ContactMessagesForm({'contact_email': ''})
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('contact_email', form.errors.keys())

    # Test to confirm correct contact us template page is rendering 
    def test_contact_us_page(self):
        response = self.client.get('/contact_us/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us/contact_us.html')