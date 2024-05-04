from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Article
from .forms import ArticleForm

def article_list(request):
    articles = Article.objects.order_by("-created_on")
    context = {"articles": articles}
    return render(request, "wiki/article_list.html", context)

@login_required
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

@login_required
def article_create(request):
    form=ArticleForm
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article()
            article.title = form.cleaned_data.get("title")
            article.category.name = form.cleaned_data.get("category")
            article = form.save()
            return redirect("wiki:article_detail", pk=article.pk)
        
    ctx = {"articleform":form}
    return render(request, 'wiki/article_create.html',ctx)

@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("wiki:article_detail", pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    
    ctx = {"articleform":form}
    return render(request, 'wiki/article_update.html',ctx)
