from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

######### accounts

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")