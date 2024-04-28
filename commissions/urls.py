from django.urls import path

from .views import commission_detail, commission_list

urlpatterns = [
    path("list", commission_list, name="list"),
    path("detail/<int:pk>", commission_detail, name="commission"),
]

app_name = "commissions"
