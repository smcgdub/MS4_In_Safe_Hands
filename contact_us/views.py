from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import ContactMessages
from .forms import ContactMessagesForm
from profiles.models import UserProfile

# Original Code 

def contact_us(request):
    # View that returns contact us page
    messages_form = ContactMessagesForm()

    if request.method == 'POST':
        messages_form = ContactMessagesForm(ContactMessages)
        if messages_form.is_valid():
            messages_form.save()
            messages.success(request, "Your message to us has been successfully sent")
            return redirect(reverse('home'))
        else:
            messages.error(request, "There was an error sending your message, please try to send it again")
            return redirect(reverse('home'))

    template = 'contact_us/contact_us.html'
    context = {
        'form': messages_form
    }
    return render(request, template, context=context)



# def contact_us(request):
#     # View that returns contact us page

#     messages_form = ContactMessagesForm()
#     profile = UserProfile.objects.get(user=request.user)

#     if request.method == "POST":
#         # if request.user.is_authenticated:
#         profile = UserProfile.objects.get(user=request.user)
#         form_data = {
#             "sender": "Sent By",
#             "subject": request.POST["subject"],
#             "message": request.POST["message"],
#             "contact_email": request.POST["contact_email"],
#             "date": request.POST["date"],
#         }
#         messages_form = ContactMessagesForm(form_data)

#     if messages_form.is_valid():
#         messages_form.save()
#         messages.success(request,
#                          'Your message to us has been successfully sent'
#                          )
#         return redirect(reverse('home'))
#     # else:
#     #     messages.error(request,
#     #                    'There was an error sending your message, please try to send it again'
#     #                    )

#     #     return redirect(reverse('home'))

#     template = 'contact_us/contact_us.html'
#     context = {'form': messages_form}

#     return render(request, template, context=context)



    # if request.method == 'POST':
    #     if request.user.is_authenticated:
    #         profile = UserProfile.objects.get(user=request.user)

    # form_data = {
    # 'sender': 'Sent By',
    #             'subject': request.POST['subject'],
    #             'message': request.POST['message'],
    #             'contact_email': request.POST['contact_email'],
    #             'date': request.POST['date'],
    #             'sender': profile,}messages_form = ContactMessagesForm(form_data)if messages_form.is_valid():