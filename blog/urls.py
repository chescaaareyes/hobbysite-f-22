from django.urls import path

from .views import ArticleDetailsView, ArticleListView

urlpatterns = [
    path("articles/", ArticleListView.as_view(), name="article_list"),
    path("article/<int:pk>/", ArticleDetailsView.as_view(), name="article_detail"),
]

app_name = "blog"
