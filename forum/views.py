from django.shortcuts import render

from .models import Post, PostCategory


def thread_list(request):
    categories = PostCategory.objects.all()
    ctx = {"categories": categories}
    return render(request, "forum/thread_list.html", ctx)


def thread_detail(request, pk):
    category = PostCategory.objects.get(pk=pk)
    posts = Post.objects.filter(category__pk=pk)
    ctx = {
        "category": category,
        "posts": posts,
    }
    return render(request, "forum/thread_detail.html", ctx)
