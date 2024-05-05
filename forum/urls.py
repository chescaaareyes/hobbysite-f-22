from django.urls import path

from .views import forum_detail, forum_list, forum_create, forum_update

urlpatterns = [
    path("threads/", forum_list, name="forum_list"),
    path("thread/<int:pk>", forum_detail, name="forum_detail"),
    path("thread/<int:pk>/add", forum_create, name="forum_create"),
    path("thread/<int:pk>/edit", forum_update, name="forum_update"),
]

app_name = "forum"
