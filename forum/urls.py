from django.urls import path

from .views import forum_detail, forum_list

urlpatterns = [
    path("threads/", forum_list, name="forum_list"),
    path("threads/<int:pk>", forum_detail, name="forum_detail"),
]

app_name = "forum"
