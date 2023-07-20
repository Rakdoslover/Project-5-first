from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Instructor


def instructors(request):
    """ A view to return the instructors page """

    return render(request, 'instructors/instructors.html')


# View for instructors page
class InstructorsList(generic.ListView):
    model = Instructor
    queryset = Instructor.objects.order_by("name")
    template_name = "instructors/instructors.html"
    
