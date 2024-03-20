from django.urls import path

from .views import product, products_list

urlpatterns = [
    path("items", products_list, name="product_list"),
    path("item/<int:pk>/", product, name="product_detail"),
]

app_name = "merchstore"
