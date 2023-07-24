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

    return render(request, 'our-sessions/our-sessions.html', context)


def session_detail(request, workout_session_id):
    """ A view to show individual session """

    workout_sessions = get_object_or_404(
        Workout_Session, pk=workout_session_id)

    context = {
        'workout_sessions': workout_sessions
    }

    return render(request, 'workouts/session-detail.html', context)
