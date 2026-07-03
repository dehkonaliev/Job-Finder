from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    STATUS = (
        ('worker', 'Worker'),
        ('employer', 'Employer')
    )
    
    role = models.CharField(max_length=10, choices=STATUS)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"