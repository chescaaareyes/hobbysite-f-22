from django.shortcuts import render

from .models import Article


def article_list(request):
    articles = Article.objects.order_by("-created_on")
    context = {"articles": articles}
    return render(request, "wiki/article_list.html", context)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "title": article.title,
        "category": article.category.name,
        "created_on": article.created_on,
        "updated_on": article.updated_on,
        "entry": article.entry,
    }
    return render(request, "wiki/article_detail.html", context)
