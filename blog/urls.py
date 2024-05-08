from django.urls import path

from . import views

urlpatterns = [
    path("articles/", views.articleList, name="article_list"),
    path("article/<int:pk>/", views.articleDetail, name="article_detail"),
    path("article/add/", views.articleCreate, name="article_create"), 
    path("article/<int:pk>/edit/", views.articleUpdate, name="article_update"),  
]

app_name = "blog"
