from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Thread, ThreadCategory, Comment


def thread_list(request):
    categories = ThreadCategory.objects.all()
    ctx = {"categories": categories}
    return render(request, "forum/thread_list.html", ctx)


def thread_detail(request, pk):
    category = ThreadCategory.objects.get(pk=pk)
    posts = Thread.objects.filter(category__pk=pk)
    ctx = {
        "category": category,
        "posts": posts,
    }
    return render(request, "forum/thread_detail.html", ctx)


@login_required
def thread_create(request, pk):
    return HttpResponse("Hello World")

@login_required
def thread_update(request, pk):
    return HttpResponse("Hello World")
