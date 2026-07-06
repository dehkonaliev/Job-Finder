from django.db import models
from jobs.models import Job
from users.models import CustomUser

class Resume(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    desired_position = models.CharField(max_length=100)
    skills = models.CharField(max_length=400)
    experience = models.IntegerField()
    education = models.CharField(max_length=200)
    bio = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    

class Application(models.Model):
    APP_STATUS = (
        ('pending', 'Pending'),
        ('viewed', 'Viewed'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected')
    )
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    worker = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    cover_letter = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(choices=APP_STATUS)
    applied_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.job} - {self.worker}"
    
    