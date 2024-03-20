from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, ArticleCategory
from django.views.generic import ListView, DetailView

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'


class ArticleDetailsView(DetailView):
    model = Article
    template_name = 'blog/article_details.html'