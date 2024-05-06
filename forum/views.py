import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from user_management.models import Profile

from .forms import CommentForm, ThreadForm
from .models import Comment, Thread, ThreadCategory


def thread_list(request):
    categories = ThreadCategory.objects.all()
    threads = Thread.objects.all()
    ctx = {
        "categories": categories,
        "threads": threads,
    }
    return render(request, "forum/thread_list.html", ctx)


def thread_detail(request, pk):
    threads = Thread.objects.all()
    thread = Thread.objects.get(pk=pk)
    comments = Comment.objects.all()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment()
            author = Profile.objects.get(pk=request.user.pk)
            new_comment.author = author
            new_comment.thread = thread
            new_comment.entry = form.cleaned_data.get("entry")
            new_comment.save()
            return redirect("forum:thread_detail", pk=pk)
    ctx = {
        "form": form,
        "threads": threads,
        "thread": thread,
        "comments": comments,
    }
    return render(request, "forum/thread_detail.html", ctx)


@login_required
def thread_create(request):
    author = Profile.objects.get(pk=request.user.pk)
    form = ThreadForm()
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            new_thread = Thread()
            new_thread.title = form.cleaned_data.get("title")
            new_thread.author = author
            new_thread.category = form.cleaned_data.get("category")
            new_thread.entry = form.cleaned_data.get("entry")
            new_thread.save()
            return redirect("forum:thread_detail", pk=new_thread.pk)
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
    thread = Thread.objects.get(pk=pk)
    form = ThreadForm()
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread.title = form.cleaned_data.get("title")
            thread.category = form.cleaned_data.get("category")
            thread.entry = form.cleaned_data.get("entry")
            thread.updated_on = datetime.datetime.now()
            thread.save()
            return redirect("forum:thread_detail", pk=thread.pk)
    new_updated_on = datetime.datetime.now()
    ctx = {
        "form": form,
        "thread": thread,
        "updated_on": new_updated_on,
    }
    return render(request, "forum/thread_update.html", ctx)
