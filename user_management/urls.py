from django.urls import path

from .views import home, register

urlpatterns = [
    path("", home, name="home"),
    path("accounts/register", register, name="register"),
]

app_name = "user_management"
