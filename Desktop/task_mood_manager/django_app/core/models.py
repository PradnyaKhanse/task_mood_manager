from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    mood = models.CharField(max_length=20, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)  # new

    def __str__(self):
        return self.title
