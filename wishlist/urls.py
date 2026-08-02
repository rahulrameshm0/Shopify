from django.urls import path
from . import views

urlpatterns = [
    path("", views.wishlist, name="wishlist"),
    path("add/<int:id>/", views.add_to_wishlist, name="add_to_wishlist"),
    path("delete/<int:id>/", views.delete_wishlist_item, name="delete_wishlist"),
]