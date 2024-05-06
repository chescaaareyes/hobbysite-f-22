from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def articleList(request):
    if request.user.is_authenticated:
        userArticles = Article.objects.filter(author=request.user).order_by("-createdOn")
        otherArticles = Article.objects.exclude(author=request.user).order_by("-createdOn")
        context = {'userArticles': userArticles, 'otherArticles': otherArticles}
    else:
        otherArticles = Article.objects.all().order_by("-createdOn")
        context = {'otherArticles': otherArticles}
    return render(request, 'blog/article_list.html', context)

def articleDetail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    authorArticles = Article.objects.filter(author=article.author).exclude(pk=pk)[:2]
    comments = Comment.objects.filter(article=article).order_by('-createdOn')
    form = CommentForm()
    return render(request, 'blog/article_detail.html', {
        'article': article,
        'authorArticles': authorArticles,
        'comments': comments,
        'form': form
    })

@login_required
def articleCreate(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.createdOn = timezone.now()
            article.save()
            return redirect('blog:article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form})

@login_required
def articleUpdate(request, articleId):
    article = get_object_or_404(Article, pk=articleId)
    if request.user != article.author:
        return HttpResponse('You are not allowed to edit this article.')
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', articleId=articleId)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_form.html', {'form': form})
