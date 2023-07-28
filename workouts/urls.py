from . import views
from django.urls import path

urlpatterns = [
    path('', views.our_sessions, name='our_sessions'),
    path('<workout_session_id>/', views.session_detail, name='session_detail'),
    path('delete/<session_id>/', views.delete_session, name='delete_session'),
]
