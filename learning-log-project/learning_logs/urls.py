"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

# this defines a namespace, can be used in like template tag:
# <a href="{% url 'learning_logs:index' %}">
app_name = 'learning_logs'
urlpatterns = [
    # Home page
    # name can be used other places like in template:
    # <a href="{% url 'learning_logs:index' %}">
    path('', views.index, name='index'),
]
