from decimal import Decimal

import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

import json

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from cart.models import Cart
from .models import Order, OrderItem
from products.models import Products


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



@login_required(login_url="signin")
def buy_now(request, product_id):

    product = get_object_or_404(
        Products,
        id=product_id
    )

    quantity = int(
        request.POST.get("quantity", 1)
    )

    total = product.price * quantity

    order = Order.objects.create(
        user=request.user,
        total_amount=total,
        status=Order.OrderStatus.PENDING,
    )

    OrderItem.objects.create(
        order=order,
        product=product,
        quantity=quantity,
        price=product.price,
    )

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET,
        )
    )

    razorpay_amount = int(total * 100)

    razorpay_order = client.order.create({
        "amount": razorpay_amount,
        "currency": "INR",
        "receipt": f"order_{order.id}",
    })

    order.razorpay_order_id = razorpay_order["id"]
    order.save()

    return render(
        request,
        "checkout/checkout.html",
        {
            "order": order,
            "razorpay_order_id": razorpay_order["id"],
            "razorpay_key_id": settings.RAZORPAY_KEY_ID,
            "amount": razorpay_amount,
            "currency": "INR",
        }
    )

@login_required(login_url="signin")
@require_POST
def verify_payment(request):

    try:
        data = json.loads(request.body)

        razorpay_payment_id = data.get("razorpay_payment_id")
        razorpay_order_id = data.get("razorpay_order_id")
        razorpay_signature = data.get("razorpay_signature")

        if not all([
            razorpay_payment_id,
            razorpay_order_id,
            razorpay_signature
        ]):
            return JsonResponse(
                {
                    "success": False,
                    "message": "Missing payment information."
                },
                status=400
            )

        # Get the order from OUR database
        order = get_object_or_404(
            Order,
            razorpay_order_id=razorpay_order_id,
            user=request.user
        )

        # Create Razorpay client
        client = razorpay.Client(
            auth=(
                settings.RAZORPAY_KEY_ID,
                settings.RAZORPAY_KEY_SECRET,
            )
        )

        # Verify Razorpay signature
        client.utility.verify_payment_signature({
            "razorpay_order_id": order.razorpay_order_id,
            "razorpay_payment_id": razorpay_payment_id,
            "razorpay_signature": razorpay_signature,
        })

        # Payment is genuine
        order.razorpay_payment_id = razorpay_payment_id
        order.razorpay_signature = razorpay_signature
        order.status = Order.OrderStatus.PAID
        order.save()

        return JsonResponse({
            "success": True,
            "message": "Payment verified successfully.",
            "order_id": order.id,
        })

    except razorpay.errors.SignatureVerificationError:
        return JsonResponse(
            {
                "success": False,
                "message": "Payment verification failed."
            },
            status=400
        )

    except Exception as e:
        return JsonResponse(
            {
                "success": False,
                "message": "Something went wrong."
            },
            status=500
        )