from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import ContactMessages
from .forms import ContactMessagesForm
from profiles.models import UserProfile

# Original Code 

# def contact_us(request):
#     # View that returns contact us page
    
#     messages_form = ContactMessagesForm()
#     # profile = UserProfile.objects.get(user=request.user)

#     if request.method == 'POST':
#         messages_form = ContactMessagesForm(ContactMessages)
#         if messages_form.is_valid():
#             messages_form.save()
#             messages.success(request, "Your message to us has been successfully sent")
#             return redirect(reverse('home'))
#         else:
#             messages.error(request, "There was an error sending your message, please try to send it again")
#             return redirect(reverse('home'))
        
#     template = 'contact_us/contact_us.html'
#     context = {
#         'form': messages_form
#     }

#     return render(request, template, context=context)


def contact_us(request):
    # View that returns contact us page
    
    # messages_form = ContactMessagesForm()

    messages_form = ContactMessagesForm(initial={'sender': UserProfile.objects.get(user=request.user)})
    
    if request.method == 'POST':
        messages_form = ContactMessagesForm(request.POST)
        sender = UserProfile.objects.get(user=request.user)
        print(sender)

        if messages_form.is_valid():
            # sender = messages_form.cleaned_data['sender']
            # sender = UserProfile.objects.get(user=request.user)
            # subject = messages_form.cleaned_data['subject']
            # message = messages_form.cleaned_data['message']
            # contact_email = messages_form.cleaned_data['contact_email']
            try:
                print("ENTERING TRY BLOCK")
                # messages_form.save(commit=False)
                # print("SAVING MESSAGE FROM COMMIT FALSE")
                # messages_form.sender = sender
                # print("ADD SENDER TO FORM")
                messages_form.save()
                print("SAVING TO DB")
                messages.success(request, "Your message to us has been successfully sent. We will be in contact as soon as possible")
                return redirect(reverse('home'))
            except Exception as e:
                print("Error in try except block: ", e) # Edited by Jo
                messages.error(request, "There was an error sending your message, please try to send it again")
                return redirect(reverse('contact_us'))
        else:
            print("Error from is form valid else block")
            messages.error(request, "There was an error sending your message, please try to send it again")
            return redirect(reverse('contact_us'))
        
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