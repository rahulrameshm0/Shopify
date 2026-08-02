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

    context ={
        "wishlist_items": wishlist_items,
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

def delete_wishlist_item(request, id):
    wishlist_item = get_object_or_404(Wishlist, id=id, user=request.user)
    wishlist_item.delete()
    return redirect("wishlist")

def clear_wishlist(request):
    Wishlist.objects.filter(user=request.user).delete()
    return redirect("wishlist")