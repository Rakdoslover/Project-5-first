from . import views
from django.urls import path


urlpatterns = [
    path('', views.InstructorsList.as_view(), name='instructors'),
]
