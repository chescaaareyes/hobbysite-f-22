from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def article_list(request):
    articles = Article.objects.order_by("-created_on")
    context = {"articles": articles}
    return render(request, "wiki/article_list.html", context)

@login_required
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article=article)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.author = request.user  
            new_comment.save()
            return redirect('wiki:article_detail', pk=pk)
        
        else:
            comment_form = CommentForm()
            
    context = {
        "title": article.title,
        "category": article.category.name,
        "created_on": article.created_on,
        "updated_on": article.updated_on,
        "entry": article.entry,
        "article": article,
        "comments": comments,
        "comment_form": comment_form,
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
            article.category = form.cleaned_data.get("category")
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
