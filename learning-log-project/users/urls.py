"""Defines URL patterns for users"""

from django.urls import path, include

from . import views

# for this app(users), the url pattern is like http://localhost:8000/users/xxx
app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    # The login page’s pattern matches the URL http://localhost:8000/users/login/, and Django also provides
    # other default urls like logout.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
]
