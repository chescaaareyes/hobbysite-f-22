from django.urls import path

from .views import product_detail, products_list, product_add, cart_view, transaction_view

urlpatterns = [
    path("items", products_list, name="product_list"),
    path("item/<int:pk>/", product_detail, name="product_detail"),
    path("item/add/", product_add, name="product_add"),
    path("cart/", cart_view, name="cart"),
    path("transactions/", transaction_view, name="transaction"),
]

app_name = "merchstore"
