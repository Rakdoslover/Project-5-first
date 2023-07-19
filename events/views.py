from django.shortcuts import render


def events(request):
    """ A view to return the index page """

    return render(request, 'events/events-page.html')
