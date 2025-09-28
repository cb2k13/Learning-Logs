"""Defines url patterns for learning_logs. """

from django.urls import path  # Imported the path function

from . import views  # Imported the views module 

app_name = 'learning_logs'
urlpatterns = [      # List of pages that can requested from the learning_logs app 
    # Home page
    path('', views.index, name='index'),  # Gives 3 arguments 
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
]
