from django.urls import path

from .views import commission_detail, commission_list, commission_create, commission_update

urlpatterns = [
    path("list", commission_list, name="commission_list"),
    path("detail/<int:pk>", commission_detail, name="commission_detail"),
    path("add", commission_create, name="commission_create"),
    path("<int:pk>/edit", commission_update, name="commission_update"),
]

app_name = "commissions"
