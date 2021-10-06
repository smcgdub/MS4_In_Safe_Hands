from django.shortcuts import render
from .models import ContactMessages
from .forms import ContactMessagesForm


def contact_us(request):
    # View that returns contact us page

    template = 'contact_us/contact_us.html'
    messages_form = ContactMessagesForm()
    context = {
        'form': messages_form
    }
    return render(request, template, context=context)