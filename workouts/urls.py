from . import views
from django.urls import path


urlpatterns = [
    path('', views.workouts, name='our-sessions'),
]
