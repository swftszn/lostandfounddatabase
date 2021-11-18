from django.db import models

# Create your models here.

class Event(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    details = models.TextField()
    