from django.shortcuts import render, redirect, get_object_or_404
from . models import Products
from django.core.paginator import Paginator

# Create your views here.

def product_list(request):
    products = Products.objects.all()

    context = {
        "Products": products
    }

    return render(request, {"context": context})


def product_details(request, id):
    product = get_object_or_404(Products, id=id)

    context = {
        "Product": product
    }

    return render(request, "shop/shopping.html", context)


def shopping(request):
    products = Products.objects.all()

    paginator = Paginator(products, 8)  # Show 8 products per page

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "shop/shopping.html", {
        "page_obj": page_obj
    })