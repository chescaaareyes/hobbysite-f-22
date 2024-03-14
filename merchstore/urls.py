from django.urls import path
from .views import product, products_list


urlpatterns = [
    path("merchstore/items", products_list, name="product_list"),
    path("merchstore/item/<int:pk>/", product, name="product_item"),
]

app_name = "merchstore"