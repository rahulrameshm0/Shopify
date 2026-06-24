from django.db import models

# Create your models here.


class Accounts(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    phone = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    confirm_password = models.CharField(max_length=150)

    def __str__(self):
        return self.username