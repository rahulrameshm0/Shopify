from django.shortcuts import render, redirect, get_object_or_404
from . models import Products
from django.core.paginator import Paginator
from categories.models import Category
from django.db.models import Count
from django.db.models import Avg

# Create your views here.

def product_list(request):
    products = Products.objects.all()

    context = {
        "products": products
    }
    return render(request, {"context": context})

def product_details(request, id):
    product = get_object_or_404(Products, id=id)

     # Get the product first
    product = get_object_or_404(Products, id=id)
    
        # Get all reviews for this product
    reviews = product.reviews.all()
    total_reviews = reviews.count()
    
    average_rating = reviews.aggregate(avg=Avg("rating"))["avg"] or 0
    
    star_counts = {}
    
    for star in range(1, 6):
        count = reviews.filter(rating=star).count()
    
        if total_reviews > 0:
            percentage = round((count / total_reviews) * 100)
        else:
            percentage = 0
            star_counts[star] = {
                "count": count,
                "percentage": percentage
            }
    
        context = {
            "product": product,
            "star_counts": star_counts,
            "average_rating": round(average_rating, 1)
        }

    return render(request, "products/products-details.html", context)

def shopping(request):
    products = Products.objects.all()

    # CATEGORY FILTER
    categories = request.GET.getlist("category")

    if categories:
        products = products.filter(category__name__in=categories)

    # BRAND FILTER
    brands = request.GET.getlist("brand")
    if brands:
        products = products.filter(brand__in=brands)

    # PRICE FILTER
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    # AVAILABILITY FILTER
    availability = request.GET.getlist("availability")

    if "instock" in availability:
        products = products.filter(stock__gt=0)

    # RATING FILTER
    rating = request.GET.get("rating")

    if rating:
        products = products.filter(rating__gte=rating)

    # PAGINATION
    paginator = Paginator(products, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "shop/shopping.html", {"page_obj": page_obj, "categories": Category.objects.all(), }, )