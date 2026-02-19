from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('event', views.event_list, name='event_list'),
    path('create/', views.create_event, name='create_event'),
    path('checkin/<uuid:qr_code>/', views.checkin_view, name='checkin'),
    path('<int:event_id>/dashboard/', views.event_dashboard, name='event_dashboard'),
    path('portaria/<uuid:qr_code>/', views.portaria_checkin, name='portaria_checkin'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='home'), name='logout'),

]