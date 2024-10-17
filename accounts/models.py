#accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

#Ta classes they might have
class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AvailableHour(models.Model):
    day_of_week = models.CharField(max_length=10)  # e.g., "Monday", "Tuesday"
    time_slot = models.CharField(max_length=20)    # e.g., "10:00-11:00"
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='available_hours')

    def __str__(self):
        return f"{self.user.username} - {self.day_of_week} {self.time_slot}"

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('ta', 'Teaching Assistant'),
    ]
    
    age = models.PositiveBigIntegerField(null=True, blank=True)
    pronouns = models.CharField(max_length=50, null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    ta_classes = models.ManyToManyField(Class, blank=True)  # TAs can teach multiple classes
    tutoring_hours = models.CharField(max_length=100, blank=True)  

    def __str__(self):
        return self.username