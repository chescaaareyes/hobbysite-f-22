from django.urls import path

from .views import thread_create, thread_detail, thread_list, thread_update

urlpatterns = [
    path("threads/", thread_list, name="thread_list"),
    path("thread/<int:pk>", thread_detail, name="thread_detail"),
    path("thread/add", thread_create, name="thread_create"),
    path("thread/<int:pk>/edit", thread_update, name="thread_update"),
]

app_name = "forum"
