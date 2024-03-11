# fsc_app/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Profile for {self.user.username}"
    
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class StripingForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    is_voice_input = models.BooleanField(default=False)
    
    # Additional fields for form details
    road_name = models.CharField(max_length=255, default='')
    white_paint_footage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    yellow_paint_footage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    size_of_white_paint_line = models.CharField(max_length=50, default='')
    size_of_yellow_paint_line = models.CharField(max_length=50, default='')

    def __str__(self):
        return f"Form submitted by {self.user.username} on {self.date_submitted} for {self.road_name}"
