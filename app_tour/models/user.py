from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    preferred_language = models.CharField(max_length=20, null=True, blank=True)
    is_vip = models.BooleanField(default=False)
    preferences = models.JSONField(default=dict)
    
