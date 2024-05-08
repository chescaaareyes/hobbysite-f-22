from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Product, ProductType, Transaction
from .forms import TransactionForm, ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser


def products_list(request):
    your_shop = []
    user_products = []
    if request.user.is_authenticated:
        logged_user = request.user.profile
        your_shop = Product.objects.filter(status = "On Sale").filter(owner = logged_user)
        for_sale = Product.objects.exclude(owner = logged_user).filter(status = "On Sale")
        user_products = Product.objects.exclude(status = "On Sale").filter(owner = logged_user)
        other_products = Product.objects.exclude(status = "On Sale").exclude(owner = logged_user)
        total_count = other_products.count() + user_products.count()
    else:
        logged_user = "Anonymous"
        for_sale = Product.objects.filter(status = "On Sale")
        other_products = Product.objects.exclude(status = "On Sale")
        total_count = other_products.count()
    
        
    ctx = {
        "username" : logged_user,
        "your_shop" : your_shop,
        "user_products": user_products,
        "others" : other_products,
        "for_sale" : for_sale,
        "all_products_count" : total_count,
    }
    return render(request, "merchstore/product_list.html", ctx)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    form = TransactionForm()
    if request.method == "POST":
        form = TransactionForm(request.POST, product=product)
        if form.is_valid():
            transact = Transaction()
            transact.product = product
            transact.amount = form.cleaned_data.get("amount")
            transact.status = 0
            if request.user.is_authenticated:
                user = request.user.profile
                transact.buyer = user
                product.stock -= transact.amount
                if product.stock == 0:
                    product.status = "Out of Stock"
                else:
                    product.status = "Available"
                product.save()
                transact.save()
                return redirect("merchstore:cart")
            else:
                return redirect("login")

    ctx = {
        "product" : product,
        "name": product.name,
        "owner" : product.owner,
        "description": product.description,
        "price": product.price,
        "product_type": product.product_type.name,
        "form" : form,
        "status" : product.status,
        "stock" : product.stock,
    }
    if request.user.is_authenticated:
        ctx["logged_user"] = request.user.profile
    return render(request, "merchstore/product_detail.html", ctx)


@login_required
def product_add(request):
    user = request.user.profile
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid:
            product = form.save()
            product.owner = user
            if product.stock == 0:
                product.status = "Out of Stock"
            product.save()
            return redirect("merchstore:product_detail", pk=product.pk)
    ctx = {
        "form" : form,
        "logged_user" : user,
    }
    return render(request, "merchstore/product_add.html", ctx)


@login_required
def product_updateview(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user.profile
    form = ProductForm(initial = {"owner" : product.owner, "product_type" : product.product_type, "price" : product.price, "name" : product.name, "stock" : product.stock, "description" : product.description,})
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid:
            product.owner = user
            if product.stock == 0:
                product.status = "Out of Stock"
            product.save()
            return redirect("merchstore:product_detail", pk=product.pk)
    ctx = {
        "form" : form,
        "logged_user" : user,
    }
    return render(request, "merchstore/product_edit.html", ctx)


@login_required
def cart_view(request):
    user = request.user.profile
    users_cart = Transaction.objects.filter(buyer = user).order_by("product__owner")
    ctx = {
        "logged_user" : user,
        "users_cart" : users_cart,
    }
    return render(request, "merchstore/cart.html", ctx)


@login_required
def transaction_view(request):
    user = request.user.profile
    users_transactions = Transaction.objects.filter(product__owner = user).order_by("buyer")
    ctx = {
        "logged_user" : user,
        "users_transactions" : users_transactions,
    }
    return render(request, "merchstore/transactions.html", ctx)