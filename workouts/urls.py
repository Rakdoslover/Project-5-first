from . import views
from django.urls import path

urlpatterns = [
    path('', views.our_sessions, name='our_sessions'),
    path('add/', views.add_session, name='add_session'),
    path('edit/<workout_session_id>/',
         views.edit_session, name='edit_session'),
    path('delete/<workout_session_id>/',
         views.delete_session, name='delete_session'),
    path('<workout_session_id>/', views.session_detail, name='session_detail'),
]
