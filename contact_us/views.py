from django.shortcuts import render


def contact_us(request):
    # View that returns contact us page
    return render(request, 'contact_us/contact_us.html')