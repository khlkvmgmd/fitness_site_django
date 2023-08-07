
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField() # Длительность тренировки в минутах

    def __str__(self):
        return self.title