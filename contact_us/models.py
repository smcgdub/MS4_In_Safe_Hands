from django.db import models
from django import forms
from profiles.models import UserProfile


class ContactMessages(models.Model):
    # Contact form model
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=80, null=False, blank=False)
    message = models.TextField(max_length=3000, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    contact_email = models.EmailField(max_length=254, null=True, blank=True)

    # This will correct the spelling in Django admin to the correct plural spelling
    class Meta:
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return self.subject