from django.shortcuts import render
from goods.models import Products
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator

def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 2)
    current_page = paginator.page(2)
    context = {
        "title": "Home - Каталог",
        #"goods": goods,
        "goods":current_page,
    }
    return render(request, "goods/catalog.html", context)


# def product(request, product_slug=False, product_id=False):
#     if product_id:
#         product = Products.objects.get(id=product_id)
#     else:
#         product = Products.objects.get(slug=product_slug)
#     context = {"product": product}
#     return render(request, "goods/product.html", context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {"product": product}
    return render(request, "goods/product.html", context)