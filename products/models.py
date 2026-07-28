from django.db import models
from categories.models import Category
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=260)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/")
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0, validators=[MinValueValidator(0),
                                                                                        MaxValueValidator(5)])
    HERO_CHOICES = [
        ("homepod", "HomePod"),
        ("watch", "Watch"),
        ("phone", "Phone"),
        ("camera", "Camera"),
        ("earbuds", "Earbuds"),
        ("dslr", "DSLR"),
    ]

    hero_position = models.CharField(
        max_length=20,
        choices=HERO_CHOICES,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return  self.name

class Specification(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="specification")
    name = models.CharField(max_length=100)
    value = models.TextField()