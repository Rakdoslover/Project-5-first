from . import views
from django.urls import path


urlpatterns = [
    path('', views.workouts, name='our_sessions'),
    path('<workout_session_id>/', views.session_detail, name='session_detail'),
]
