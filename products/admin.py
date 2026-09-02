from django.contrib import admin
from .models import Products, Specification, TrendingProduct

# Register your models here.
admin.site.register(Products)
admin.site.register(TrendingProduct)
