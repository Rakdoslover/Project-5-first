from django.shortcuts import render

# Create your views here.
def contact_page(request):
    """ A view that renders the contact page """

    return render(request, 'contact/contact.html')
