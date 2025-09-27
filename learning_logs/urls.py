"""Defines url patterns for learning_logs. """

from django.urls import path  # Imported the path function

from . import views  # Imported the views module 

app_name = 'learning_logs'
urlspatterns = [
    # Home page
    path('', views.index, name='index')
]