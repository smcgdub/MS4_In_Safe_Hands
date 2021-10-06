from django.contrib import admin
from .models import ContactMessages


class ContactMessagesAdmin(admin.ModelAdmin):
    list_display = (
      'sender',
      'subject',
      'date',
      'contact_email',
    )

    ordering = ('date',)

admin.site.register(ContactMessages, ContactMessagesAdmin)
