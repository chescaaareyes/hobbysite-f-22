from django.urls import path

from . import views

urlpatterns = [
    path("articles/", views.articleList, name="article_list"),
    path("article/<int:pk>/", views.articleDetail, name="article_detail"),
]

app_name = "blog"
