from django import forms
from django.forms import ModelForm
from .models import ContactMessages
from django.forms import HiddenInput


class ContactMessagesForm(forms.ModelForm):
    class Meta:
        # exclude('sender',)
        model = ContactMessages
      # Fields to dispaly on the contact us form
        # fields = ('sender', 'subject', 'message', 'contact_email')
        fields = ('sender', 'subject', 'message', 'contact_email')
        widgets={'sender': HiddenInput()}


    def __init__(self, *args, **kwargs):
        # Placeholders to be added to the checkout fields
        super().__init__(*args, **kwargs)
        placeholders = {
            'sender': 'Sent by',
            'subject': 'Message subject',
            'message': 'Your message',
            'contact_email': 'Your email address',
            # 'date': 'Date & Time',
            }

        # Form will auto start on subject
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