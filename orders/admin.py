from django.contrib import admin
from . models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "total_amount",
        "status",
        "razorpay_order_id",
        "created_at",
    )

    list_filter = ("status", "created_at")

    search_fields = (
        "razorpay_order_id",
        "razorpay_payment_id",
        "user__username",
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "product",
        "quantity",
        "price",
    )