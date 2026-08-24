from decimal import Decimal

import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cart.models import Cart
from .models import Order, OrderItem


@login_required(login_url="signin")
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect("cart")

    # Calculate total from the database
    total = Decimal("0.00")

    for item in cart_items:
        total += item.product.price * item.quantity

    # Create our Django Order
    order = Order.objects.create(
        user=request.user,
        total_amount=total,
        status=Order.OrderStatus.PENDING,
    )

    # Create OrderItems
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )

    # Create Razorpay client
    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET,
        )
    )

    # Razorpay expects amount in paise
    razorpay_amount = int(total * 100)

    razorpay_order = client.order.create(
        {
            "amount": razorpay_amount,
            "currency": "INR",
            "receipt": f"order_{order.id}",
        }
    )

    # Save Razorpay Order ID in our database
    order.razorpay_order_id = razorpay_order["id"]
    order.save()

    return render(request, "orders/checkout.html", {
        "order": order,
        "razorpay_order_id": razorpay_order["id"],
        "razorpay_key_id": settings.RAZORPAY_KEY_ID,
        "amount": razorpay_amount,
        "currency": "INR",
    })