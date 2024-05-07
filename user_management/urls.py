from django.urls import path

from .views import home, register, update_profile, user_profile

urlpatterns = [
    path("", home, name="home"),
    path("accounts/register", register, name="register"),
    path("accounts/profile", user_profile, name="profile"),
    path("accounts/update", update_profile, name="update"),
]

app_name = "user_management"
