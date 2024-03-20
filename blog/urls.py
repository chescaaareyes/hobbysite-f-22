from django.urls import path

from .views import ArticleListView, ArticleDetailsView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetailsView.as_view(), name='article_details'), ]

app_name = "blog"