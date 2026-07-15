from django.db import models
from categories.models import Category
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=260)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/")
    description = models.TextField()

    def __str__(self):
        return  self.name