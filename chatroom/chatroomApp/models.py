from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    # Owner of Message
    owner = models.ForeignKey(User);

    # Time and text of message
    date = models.DateTimeField()
    text = models.CharField(max_length=250)