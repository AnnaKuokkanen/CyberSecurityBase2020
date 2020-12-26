from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    participants = models.ManyToManyField(Participant)