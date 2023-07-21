from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Instructor


def instructors(request):
    """ A view to return the instructors page """

    instructors = Instructor.objects.all()

    context = {
        'instructors': instructors
    }

    return render(request, 'instructors/instructors.html', context)
