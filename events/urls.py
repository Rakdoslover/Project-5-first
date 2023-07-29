from . import views
from django.urls import path

urlpatterns = [
    path('', views.events, name='events'),
    path('add/', views.add_event, name='add_event'),
    path('edit/<event_id>/', views.edit_event, name='edit_event'),
    path('delete/<event_id>/', views.delete_event, name='delete_event'),
    path('<event_id>/', views.event_detail, name='event_detail'),
]
