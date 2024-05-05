from django.urls import path

from .views import thread_detail, thread_list

urlpatterns = [
    path("threads/", thread_list, name="thread_list"),
    path("thread/<int:pk>", thread_detail, name="thread_detail"),
]

app_name = "forum"
