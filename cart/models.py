from django.db import models
from django.contrib.auth.models import User
from products.models import Products

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")

    @property    
    def subtotal(self):
        return self.product.price * self.quantity


    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
