from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cart/", views.cart, name="cart"),
    path("contacts/", views.contacts, name="contacts"),
    path("shopping/", views.shop, name="shopping"),
    path("products/", views.products, name="products"),
    path("about/", views.about, name="about"),
    # path("wishlist/", views.wishlist, name="wishlist"),
]