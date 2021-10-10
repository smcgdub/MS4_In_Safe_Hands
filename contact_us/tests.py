from django.test import TestCase
from .forms import ContactMessagesForm


class TestContactMessagesForm(TestCase):

    # Test to confirm correct contact us template page is rendering 
    def test_contact_us_page(self):
        response = self.client.get('/contact_us/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us/contact_us.html')

    # Test to confirm that 'sender' field is required on the message form. This field autopopulates with the users username on so it shouldn't be able to leave this blank
    def test_contact_us_form_sender_required(self):
        form = ContactMessagesForm({'sender': ''})
        self.assertFalse(form.is_valid())

    # Test to confirm that the 'subject' field is required on the message form. A user must input a subject manually in this field. 
    def test_contact_us_form_subject_required(self):
        form = ContactMessagesForm({'subject': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())

    # Test to confirm that the 'message' field is required on the message form. A user must input a message manually in this field. 
    def test_contact_us_form_message_required(self):
        form = ContactMessagesForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())

    # Test to confirm that the 'contact email' field is not required on the message form and the form will send if the field is left blank
    def test_contact_us_form_email_not_required(self):
        form = ContactMessagesForm({
                                    'subject': 'subject',
                                    'message': 'message',
                                    'contact_email': ''
                                  })
        self.assertTrue(form.is_valid())
