from django.urls import path

from .views import article_detail, article_list, article_create, article_update

urlpatterns = [
    path("articles", article_list, name="article_list"),
    path("article/<int:pk>/", article_detail, name="article_detail"),
    path('article/add/', article_create, name="article_create"),
    path('article/<int:pk>/edit', article_update, name="article_update"),

]

app_name = "wiki"
