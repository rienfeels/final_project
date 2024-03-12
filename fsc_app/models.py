from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='')

    def save(self, *args, **kwargs):
        # Custom validation logic
        if User.objects.filter(email=self.email).exclude(id=self.user.id if self.user.id else None).exists():
            raise ValueError('This email address is already in use.')

        super(UserProfile, self).save(*args, **kwargs)
    
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class DailyReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_submitted = models.DateTimeField(auto_now_add=True)
    road_name = models.CharField(max_length=255, default='')
    contractor = models.CharField(max_length=255, default='')
    workers = models.IntegerField()
    job_time_arrived = models.TimeField()
    job_time_finished = models.TimeField()
    color = models.CharField(max_length=10)  # "white" or "yellow"
    material = models.CharField(max_length=10)  # "paint" or "thermo"
    line_type = models.CharField(max_length=10)  # "solid" or "skip"
    white_footage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    white_size = models.CharField(max_length=50, default='')
    yellow_footage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    yellow_size = models.CharField(max_length=50, default='')
    dot_employee = models.BooleanField(default=False)
    # Add other fields as needed

    def __str__(self):
        return f"Form submitted by {self.user.username} on {self.date_submitted} for {self.road_name}"