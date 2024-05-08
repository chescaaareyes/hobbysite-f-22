from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from user_management.models import Profile

from .forms import ArticleForm, CommentForm
from .models import Article, Comment


def articleList(request):
    if request.user.is_authenticated:
        userArticles = Article.objects.filter(
            author=Profile.objects.get(user=request.user)
        ).order_by("-createdOn")
        otherArticles = Article.objects.exclude(
            author=Profile.objects.get(user=request.user)
        ).order_by("-createdOn")
        context = {"userArticles": userArticles, "otherArticles": otherArticles}
    else:
        otherArticles = Article.objects.all().order_by("-createdOn")
        context = {"otherArticles": otherArticles}
    return render(request, "blog/article_list.html", context)


def articleDetail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    authorArticles = Article.objects.filter(author=article.author).exclude(pk=pk)[:2]
    comments = Comment.objects.filter(article=article).order_by("-createdOn")

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect("blog:article_detail", pk=pk)
    else:
        form = CommentForm()

    context = {
        "article": article,
        "authorArticles": authorArticles,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/article_detail.html", context)


@login_required
def articleCreate(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = Profile.objects.get(user=request.user)
            article.createdOn = timezone.now()
            article.save()
            return redirect("blog:article_detail", pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, "blog/article_form.html", {"form": form})


@login_required
def articleUpdate(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user != article.author.user:
        return HttpResponse("You are not authorized to edit this article.")
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("blog:article_detail", pk=pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, "blog/article_form.html", {"form": form})
