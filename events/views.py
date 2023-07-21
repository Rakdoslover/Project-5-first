from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Event
from django.urls import reverse_lazy


def events(request):
    """ A view to return the events page """

    events = Event.objects.all()

    context = {
        'events': events
    }

    return render(request, 'events/events.html', context)
