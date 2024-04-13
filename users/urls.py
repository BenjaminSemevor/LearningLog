"""Defines URL patterns for users"""

from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
    # Logout URL with redirection to homepage (index).
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
]