
from django.db import models
from django.contrib.auth.models import User
from products.models import Products

# Create your models here.

class Reviews(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"