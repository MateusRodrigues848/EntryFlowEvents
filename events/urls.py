from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('create/', views.create_event, name='create_event'),
    path('checkin/<uuid:qr_code>/', views.checkin_view, name='checkin'),
    path('<int:event_id>/dashboard/', views.event_dashboard, name='event_dashboard'),
    path('portaria/<uuid:qr_code>/', views.portaria_checkin, name='portaria_checkin'),

]