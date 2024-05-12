from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

from user_management.models import Profile


def article_list(request):
    articles = Article.objects.order_by("-created_on")
    user_articles = (
        articles.filter(author=Profile.objects.get(user=request.user)) if request.user.is_authenticated else []
    )
    other_articles = (
        articles.exclude(author=Profile.objects.get(user=request.user))
        if request.user.is_authenticated
        else articles
    )
    ctx = {"user_articles": user_articles, "other_articles": other_articles}
    return render(request, "wiki/article_list.html", ctx)


@login_required
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article=article)
    comment_form = CommentForm()
    related_articles = Article.objects.filter(category=article.category).exclude(pk=pk)[
        :2
    ]
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.author = Profile.objects.get(user=request.user)
            new_comment.save()
            return redirect("wiki:article_detail", pk=pk)

    ctx = {
        "author": article.author,
        "title": article.title,
        "category": article.category,
        "created_on": article.created_on,
        "updated_on": article.updated_on,
        "entry": article.entry,
        "article": article,
        "comments": comments,
        "comment_form": comment_form,
        "related_articles": related_articles,
    }
    return render(request, "wiki/article_detail.html", ctx)


@login_required
def article_create(request):
    form = ArticleForm
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = Profile.objects.get(user=request.user)
            article = form.save()
            return redirect("wiki:article_detail", pk=article.pk)

    ctx = {"articleform": form}
    return render(request, "wiki/article_update.html", ctx)


@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            form.save()
            return redirect("wiki:article_detail", pk=article.pk)
    else:
        form = ArticleForm(instance=article)

    ctx = {"articleform": form}
    return render(request, "wiki/article_update.html", ctx)
