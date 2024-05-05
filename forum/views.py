from django.shortcuts import render

from .models import Thread, ThreadCategory, Comment


def thread_list(request):
    categories = ThreadCategory.objects.all()
    ctx = {"categories": categories}
    return render(request, "forum/forum_list.html", ctx)


def forum_detail(request, pk):
    category = ThreadCategory.objects.get(pk=pk)
    posts = Thread.objects.filter(category__pk=pk)
    ctx = {
        "category": category,
        "posts": posts,
    }
    return render(request, "forum/forum_detail.html", ctx)
