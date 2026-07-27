from django.shortcuts import render, redirect, get_object_or_404
from products.models import Products
from . models import Cart

# Create your views here.

def add_to_cart(request, id):
    product = get_object_or_404(Products, id=id)

    cart_item, created = Cart.objects.get_or_create(
        user = request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")

def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = 0
    quantity = 0

    for item in cart_items:
        total += item.product.price * item.quantity
        quantity += item.quantity

    return render(request, "cart/cart.html", {
        "cart_items": cart_items,
        "total": total,
        "quantity": quantity
    })


def subtotal(self):
    return self.product.price * self.quantity

def increase_quantity(request, id):
    cart_item = get_object_or_404(Cart, id=id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()

    return redirect("cart")


def decrease_quantity(request, id):
    cart_item = get_object_or_404(Cart, id=id, user=request.user)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect("cart")


def delete_cart_items(request, id):
    cart_items = get_object_or_404(Cart, id=id, user=request.user)
    cart_items.delete()
    return redirect("cart")