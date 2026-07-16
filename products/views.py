from django.shortcuts import render, redirect, get_object_or_404
from . models import Products
from django.core.paginator import Paginator

# Create your views here.

def product_list(request):
    products = Products.objects.all()

    context = {
        "products": products
    }
    return render(request, {"context": context})

def product_details(request, id):
    product = get_object_or_404(Products, id=id)

    context = {
        "product": product
    }

    return render(request, "shop/shopping.html", context)