from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Accounts(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    # phone = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    confirm_password = models.CharField(max_length=150)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"