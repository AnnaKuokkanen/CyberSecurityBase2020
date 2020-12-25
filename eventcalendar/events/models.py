from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    firsname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    

class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    partícipants = models.ManyToManyField(User)