from django.urls import path

from .views import commission, commissions_list

urlpatterns = [
    path("list", commissions_list, name="list"),
    path("detail/<int:pk>", commission, name="commission"),
]

app_name = "commissions"
