from django.shortcuts import render

from .models import Post, PostCategory


def forum_list(request):
    categories = PostCategory.objects.all()
    ctx = {"categories": categories}
    return render(request, "forum/forum-list.html", ctx)


def forum_detail(request, pk):
    category = PostCategory.objects.get(pk=pk)
    posts = Post.objects.filter(category__pk=pk)
    ctx = {
        "category": category,
        "posts": posts,
    }
    return render(request, "forum/forum-detail.html", ctx)
