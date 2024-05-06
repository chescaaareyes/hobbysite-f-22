from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Article List View
def articleList(request):
    if request.user.is_authenticated:
        userArticles = Article.objects.filter(author=request.user.profile)
        allArticles = Article.objects.exclude(author=request.user.profile)
        context = {'userArticles': userArticles, 'allArticles': allArticles}
    else:
        allArticles = Article.objects.all()
        context = {'allArticles': allArticles}
    return render(request, 'blog/article_list.html', context)

# Article Detail View
def articleDetail(request, articleId):
    article = get_object_or_404(Article, pk=articleId)
    authorArticles = Article.objects.filter(author=article.author).exclude(pk=articleId)[:2]
    comments = Comment.objects.filter(article=article).order_by('-createdOn')
    form = CommentForm()
    return render(request, 'blog/article_detail.html', {
        'article': article,
        'authorArticles': authorArticles,
        'comments': comments,
        'form': form
    })

# Article Create View
@login_required
def articleCreate(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user.profile
            article.save()
            return redirect('article_detail', articleId=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form})

# Article Update View
@login_required
def articleUpdate(request, articleId):
    article = get_object_or_404(Article, pk=articleId)
    if request.user.profile != article.author:
        return HttpResponse('You are not allowed to edit this article.')
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', articleId=articleId)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_form.html', {'form': form})
