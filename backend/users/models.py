from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=30)
    otp = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    mobile_verified = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=CASCADE, related_name='user_profile_data')
    profile_photo = models.ImageField(upload_to = 'user/images', blank=True, null=True)
    about = models.CharField(max_length=200, blank=True, null=True)
