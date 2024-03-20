from django.urls import path

from .views import article_detail, articles_list_view

urlpatterns = [
    path("articles", articles_list_view, name="article_list"),
    path("article/<int:pk>/", article_detail, name="article_detail"),
]

app_name = "wiki"
