from django.shortcuts import render


def forum_list(request):
    ctx = {
        "categories": [
            "Gaming",
            "Lifestyle",
            "Anime",
        ],
    }
    return render(request, "forum/forum-list.html", ctx)


def forum_detail(request):
    ctx = {
        "posts": [
            "Lorem Ipsum",
            "Hello World",
        ],
    }
    return render(request, "forum/forum-detail.html", ctx)
