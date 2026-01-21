from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    skills = models.TextField(help_text="comma separated skills")

    def __str__(self):
        return self.full_name
    
class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    college = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.college
    
class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)

    def __str__(self):
        return self.title
