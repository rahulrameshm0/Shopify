from django.shortcuts import render
from products.models import Products
from categories.models import Category
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    return render(request, "home/home.html")


def products(request):
    return render(request, "products/products-details.html")


def shop(request):
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
    paginator = Paginator(products, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "shop/shopping.html", {"page_obj": page_obj, "categories": Category.objects.all(), }, )

def cart(request):
    return render(request, "cart/cart.html")

def contacts(request):
    return render(request, "contacts/contacts.html")

def wishlist(request):
    return render(request, "wishlist/wishlist.html")