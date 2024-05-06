import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from user_management.models import Profile

from .forms import ThreadForm
from .models import Comment, Thread, ThreadCategory


def thread_list(request):
    categories = ThreadCategory.objects.all()
    threads = Thread.objects.all()
    ctx = {"categories": categories, "threads": threads}
    return render(request, "forum/thread_list.html", ctx)


def thread_detail(request, pk):
    category = ThreadCategory.objects.get(pk=pk)
    posts = Thread.objects.filter(category__pk=pk)
    ctx = {"category": category, "posts": posts}
    return render(request, "forum/thread_detail.html", ctx)


@login_required
def thread_create(request):
    author = Profile.objects.get(pk=request.user.pk)
    form = ThreadForm(
        initial={
            "author": author,
        }
    )
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            new_thread = Thread()
            new_thread.title = form.cleaned_data.get("title")
            new_thread.author = author
            new_thread.category = form.cleaned_data.get("category")
            new_thread.entry = form.cleaned_data.get("entry")
            new_thread.save()
            return redirect("forum:thread_list")
    new_created_on = datetime.datetime.now()
    new_updated_on = datetime.datetime.now()
    ctx = {
        "form": form,
        "created_on": new_created_on,
        "updated_on": new_updated_on,
        "author": author,
    }
    return render(request, "forum/thread_create.html", ctx)


@login_required
def thread_update(request, pk):
    return HttpResponse("Hello World")
