from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Workout_Session


def workouts(request):
    """ A view to return the our sessions page """

    workout_sessions = Workout_Session.objects.all()

    context = {
        'workout_sessions': workout_sessions
    }

    return render(request, 'our-sessions/our-sessions.html', context)
