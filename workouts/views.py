from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import generic, View
from .models import Workout_Session


def workouts(request):
    """ A view to return the our sessions page """

    workout_sessions = Workout_Session.objects.all()

    context = {
        'workout_sessions': workout_sessions
    }

    return render(request, 'our_sessions/our_sessions.html', context)


def session_detail(request, workout_session_id):
    """ A view to show individual session details """

    workout_session = get_object_or_404(
        Workout_Session, pk=workout_session_id)

    context = {
        'workout_session': workout_session
    }

    return render(request, 'our_sessions/session_detail.html', context)
