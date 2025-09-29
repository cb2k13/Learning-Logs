from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """A topic that the user is learning about"""
    text = models.CharField(max_length=200)  # Use to store small amount of text
    date_added = models.DateTimeField(auto_now_add=True)  # Piece of data to record date and time 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        """Return a string representation of the model"""
        return self.text  # Return value assigned to the text atttribute 
    

class Entry(models.Model):
    """Something specified learned about a topic"""
    # Each topic is assigned a key
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # Rferecne to anothe rrecord in the database 
    # CASCADE argument tells Django that when a topic is deleted, all entries with that topic is deleted
    text = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)

    # Holds extra info for managing a model
    class Meta:
        verbose_name_plural = 'entries'
    

    def __str__(self):
        """Return a simple string representing the entry"""
        return f"{self.text[:50]}... " # Return just first 50 characters of txt

