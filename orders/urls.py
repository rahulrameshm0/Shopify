from django.urls import path
from . import views

urlpatterns = [
    path("", views.checkout, name="checkout"),
    path("buy-now/<int:product_id>/", views.buy_now, name="buy_now")
]


