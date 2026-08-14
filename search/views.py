from django.shortcuts import render
from products.models import Products
from django.db.models import Q
from django.core.paginator import Paginator
from categories.models import Category

# Create your views here.

def search(request):
    query = request.GET.get("q", "")

    products = Products.objects.filter(
        Q(name__icontains=query) |
        Q(brand__icontains=query) |
        Q(description__icontains=query)
    )

    # Pagination
    paginator = Paginator(products, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "categories": Category.objects.all(),
        "query": query,
    }
    return render(request, "shop/shopping.html", context)
