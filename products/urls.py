from django.urls import path
from . import  views
urlpatterns = [
    path("", views.shopping, name="shop"),
    path("product-details/<int:id>", views.product_details, name="product_details"),
]