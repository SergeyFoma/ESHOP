from django.shortcuts import render
from goods.models import Products
from django.shortcuts import get_list_or_404

from django.core.paginator import Paginator
from goods.utils import q_search


# def catalog(request, category_slug, page=1):
def catalog(request, category_slug=None):

    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)  # Товары по акции
    order_by = request.GET.get(
        "order_by", None
    )  # От дешевых к дорогим От дорогих к дешевым
    query = request.GET.get("q", None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)

    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    # current_page = paginator.page(1)
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        # "goods": goods,
        "goods": current_page,
        "slug_url": category_slug,
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


from goods.models import Categories


def home(request):
    categ = Categories.objects.all()
    context = {
        "categ": categ,
    }
    return render(request, "goods/home.html", context)


def catalog2(request):

    product = Products.objects.all()

    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    quantity = request.GET.get("quantity", None)

    if on_sale:
        product = product.filter(discount__gt=0)
    if order_by:
        product = product.order_by(order_by)
    if quantity:
        product = product.filter(quantity__gt=3)

    context = {
        "product": product,
    }
    return render(request, "goods/catalog2.html", context)


def product2(request, product2_slug):
    product = Products.objects.get(slug=product2_slug)
    context = {"product": product}
    return render(request, "goods/product2.html", context)
