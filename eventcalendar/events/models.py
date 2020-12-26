from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Participant(models.Model):
    username = models.CharField(max_length=150, default='', unique=True)
class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    participants = models.ManyToManyField(Participant)