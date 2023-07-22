from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Workout_Session


def workouts(request):
    """ A view to return the our sessions page """

    return render(request, 'our-sessions/our-sessions.html')


