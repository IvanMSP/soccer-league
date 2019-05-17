#Django Libraries
from django.db import models
from django.contrib.auth.models import AbstractUser

#reusable app
from reusable.constants import *

#Pambolero 
from league.models import League
from .choices import GENDER_CHOICES


class User(AbstractUser):
    is_admin_league = models.BooleanField(default=False)
    is_admin_team = models.BooleanField(default=False)
    is_user_app = models.BooleanField(default=False)
    photo_profile = models.ImageField(
        upload_to='photo_profile',
        default='/profile/default.png',
        **NULL 
    )
    genre = models.CharField(
        max_length=100, 
        choices=GENDER_CHOICES, 
        **NULL
    )


class AdminLeagueProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        primary_key=True
    )
    league = models.OneToOneField(
        League, 
        on_delete=models.CASCADE
    )