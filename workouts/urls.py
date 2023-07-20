from . import views
from django.urls import path


urlpatterns = [
    path('', views.WorkoutsList.as_view(), name='our-sessions'),
]
