from django.shortcuts import render
from products.models import Products
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    return render(request, "home/home.html")

def products(request):
    return render(request, "products/products-details.html")

def shop(request):
    products = Products.objects.all()
    paginator = Paginator(products, 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,"shop/shopping.html",{"page_obj": page_obj })
    # return render(request, "shop/shopping.html")

def cart(request):
    return render(request, "cart/cart.html")

def contacts(request):
    return render(request, "contacts/contacts.html")

def wishlist(request):
    return render(request, "wishlist/wishlist.html")