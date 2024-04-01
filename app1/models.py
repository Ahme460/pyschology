from typing import Iterable
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from PIL import Image
from django.db.models.signals import post_save

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('instructor', 'instructor'),
        ('person', 'Someone who wants treatment'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='normal_user')
    def save(self, *args, **kwargs):
        kwargs['using'] = kwargs.get('using', 'default')
        super().save(*args, **kwargs)
        
            



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    ROLE_CHOICES = CustomUser.ROLE_CHOICES
    typee = models.CharField(max_length=30, choices=ROLE_CHOICES, default='student')
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    experience = models.TextField()
    certificates = models.TextField()
    image = models.ImageField(upload_to='profile_pic')

    about_me = models.TextField(default='')
    def __str__(self) -> str:
        return self.username
    
    def save(self, *args, **kwargs):
        kwargs['force_insert'] = kwargs.get('force_insert', False)
        super().save(*args, **kwargs)
        if self.image and hasattr(self.image, 'path') and self.image.path != 'default.jpg':  # Check if image is not default.jpg
            try:
                img = Image.open(self.image.path)
                if img.width > 300 or img.height > 300:
                    dimension = (300, 300)
                    img.thumbnail(dimension)
                    img.save(self.image.path)
            except FileNotFoundError:
                pass  # Handle the case where the file doesn't exist

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            typee=instance.role,
            username=instance.username,
            email=instance.email
        )

post_save.connect(create_profile, sender=CustomUser)

