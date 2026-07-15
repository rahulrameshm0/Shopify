from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("cart/", views.cart, name="cart"),
    path("contacts/ ", views.contacts, name="contacts"),
    path("shopping/", views.shop, name="shopping"),
    path("products/", views.products, name="products"),
    path("wishlist/", views.wishlist, name="wishlist"),
]