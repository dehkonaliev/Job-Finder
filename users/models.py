from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    STATUS = (
        ('worker', 'Worker'),
        ('employer', 'Employer')
    )
    
    role = models.CharField(max_length=10, choices=STATUS)
    phone = models.CharField(max_length=20)
    profile_img = models.ImageField(upload_to='avtrs/', blank=True, default='avtrs/default_avtr.jpg')
    
    def __str__(self):
        return self.username