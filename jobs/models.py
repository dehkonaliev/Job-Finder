from django.db import models
from users.models import CustomUser


class Company(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    website = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.owner.first_name} | {self.name}"
    
    

class Job(models.Model):
    JOBTYPES = (
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('remote', 'Remote'),
        ('internship', 'Internship'),
    )
    
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    category = models.CharField(max_length=30)
    location = models.CharField(max_length=150)
    salary_min = models.DecimalField(max_digits=20, decimal_places=2)
    salary_max = models.DecimalField(max_digits=20, decimal_places=2)
    job_type = models.CharField(max_length=20, choices=JOBTYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    