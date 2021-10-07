from django import forms
from django.forms import ModelForm
from .models import ContactMessages
# from .models import ContactForm


class ContactMessagesForm(forms.ModelForm):
    class Meta:
        # exclude('sender',)
        model = ContactMessages
      # Fields to dispaly on the contact us form
        fields = ('subject', 'message', 'contact_email')


    def __init__(self, *args, **kwargs):
        # Placeholders to be added to the checkout fields
        super().__init__(*args, **kwargs)
        placeholders = {
            'sender': 'Sent By',
            'subject': 'Message Subject',
            'message': 'Your Message',
            'contact_email': 'Your email address',
            'date': 'Date & Time',
            }

        # Form will auto start on first name
        self.fields['subject'].widget.attrs['autofocus'] = True
        for field in self.fields:
                # Asterisk will appear on required fields
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # Set placeholders 
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Labels set to false as they are not being used 
            self.fields[field].label = False