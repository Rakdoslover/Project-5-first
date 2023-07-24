from . import views
from django.urls import path


urlpatterns = [
    path('', views.workouts, name='our_sessions'),
    path('<int:workout_session_name>/', views.session_detail, name='session_detail'),
]
