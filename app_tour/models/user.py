from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    preferred_language = models.CharField(max_length=20, null=True, blank=True)
    is_vip = models.BooleanField(default=False)
    preferences = models.JSONField(default=dict)
    picture = models.ImageField(upload_to="images/", null=True)
    gender = models.CharField(max_length=6, null=True, blank=True)
    born_day = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)