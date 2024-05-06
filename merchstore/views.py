from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Product, ProductType, Transaction
from .forms import TransactionForm, ProductForm
from django.contrib.auth.decorators import login_required

# @login_required
def products_list(request):
    your_shop = []
    user_products = []
    if request.user.is_authenticated:
        username = request.user.profile
        your_shop = Product.objects.filter(status = "on sale").filter(owner = request.user.profile)
        for_sale = Product.objects.exclude(owner = request.user.profile).filter(status = "on sale")
        user_products = Product.objects.exclude(status = "on sale").filter(owner = request.user.profile)
        other_products = Product.objects.exclude(status = "on sale").exclude(owner = request.user.profile)
    else:
        username = "Anonymous"
        for_sale = Product.objects.filter(status = "on sale")
        other_products = Product.objects.exclude(status = "on sale")
        
    ctx = {
        "username" : username,
        "your_shop" : your_shop,
        "user_products": user_products,
        "others" : other_products,
        "for_sale" : for_sale,
    }
    return render(request, "merchstore/product_list.html", ctx)

@login_required
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user.profile

    form = TransactionForm()
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transact = Transaction()
            transact.buyer = user
            transact.created_on = timezone.now()
            transact.product = product
            transact.amount = form.cleaned_data.get("amount")
            transact.status = "on cart"
            transact.save()
            return redirect("user_management:home")
    ctx = {
        "logged_user" : user,
        "product" : product,
        "name": product.name,
        "owner" : product.owner,
        "description": product.description,
        "price": product.price,
        "product_type": product.product_type.name,
        "form" : form,
    }
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
            product.save()
            return redirect("merchstore:product_detail", pk=product.pk)
    ctx = {
        "form" : form,
        "logged_user" : user,
    }
    return render(request, "merchstore/product_add.html", ctx)


@login_required
def product_updateview(request, pk):
    user = request.user.profile
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("merchstore:product_edit", pk=product.pk)
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