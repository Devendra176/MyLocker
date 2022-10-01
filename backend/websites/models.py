from django.db.models import CASCADE
from django.db import models

from users.models import CustomUser

PRIVACY_CHOICE = (
    ('public', 'Public'),
    ('only_me', 'Only Me'),
)
class WebsitesData(models.Model):
    user = models.ForeignKey(CustomUser,  on_delete=CASCADE, related_name='user_website_data')
    website_url = models.URLField(max_length = 200, null=True, blank=True,)
    website_name = models.CharField(max_length=30, null=True, blank=True,)
    website_image = models.ImageField(upload_to = 'website/images', blank=True, null=True)
    website_username = models.CharField(max_length=200, null=True, blank=True,)
    website_password = models.CharField(max_length=200, null=True, blank=True,)
    website_note = models.TextField(blank=True, null=True)
    privacy = models.CharField(max_length=30, choices=PRIVACY_CHOICE, default='only_me')