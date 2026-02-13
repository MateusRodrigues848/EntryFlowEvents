from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    path('', views.event_list, name='event_list'),
]

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
