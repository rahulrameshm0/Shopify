from django.shortcuts import render
from products.models import Products

# Create your views here.

def home(request):
    hero_products = {
        product.hero_position: product
        for product in Products.objects.exclude(hero_position__isnull=True)
    }
    print(hero_products.keys())
    return render(request, "home/home.html", {"hero_products": hero_products})

def products(request):
    return render(request, "products/products-details.html")

def shop(request):
    return render(request, "shop/shopping.html")

def cart(request):
    return render(request, "cart/cart.html")

def contacts(request):
    return render(request, "contacts/contacts.html")

def wishlist(request):
    return render(request, "wishlist/wishlist.html")

def about(request):
    return render(request, "about/about.html")