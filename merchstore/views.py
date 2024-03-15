from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, ProductType


def products_list(request):
    products = Product.objects.all()
    ctx = {"products_list": products}
    return render(request, "product_list.html", ctx)


def product(request, pk):
    product = Product.objects.get(pk=pk)
    ctx = {
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "product_type": product.product_type.name,
    }
    return render(request, "product_detail.html", ctx)
