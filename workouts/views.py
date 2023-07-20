from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Workout_Session


def workouts(request):
    """ A view to return the our sessions page """

    return render(request, 'our-sessions/our-sessions.html')


# View for instructors page
class WorkoutsList(generic.ListView):
    model = Workout_Session
    queryset = Workout_Session.objects.order_by("name")
    template_name = "our-sessions/our-sessions.html"
