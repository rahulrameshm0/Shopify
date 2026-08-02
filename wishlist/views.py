from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Products
# Create your views here.

@login_required(login_url="signin")
def wishlist(request):
    wishlist_items = (
        Wishlist.objects.filter(user=request.user).select_related("products")
    )

    print("Logged in user:", request.user)
    print("Wishlist count:", wishlist_items.count())

    for item in wishlist_items:
        print(item.user, item.products.name)

    context ={
        "wishlist_items": wishlist_items,
        "quantity": wishlist_items.count()
    }

    return render(request, "wishlist/wishlist.html", context)

@login_required(login_url="signin")
def add_to_wishlist(request, id):
    product = get_object_or_404(Products, id=id)

    Wishlist.objects.get_or_create(
        user = request.user,
        products = product
    )

    return redirect(request.META.get("HTTP_REFERER", "/"))