from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    is_moderator = models.BooleanField(default=False)