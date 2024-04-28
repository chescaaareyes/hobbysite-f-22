from django.shortcuts import render

from .models import Comment, Commission


def commission_list(request):
    commissions = Commission.objects.all()
    ctx = {"commissions": commissions}
    return render(request, "commissions/commission_list.html", ctx)


def commission_detail(request, pk):
    commission_title = Commission.objects.get(pk=pk)
    comments = Comment.objects.filter(commission__pk=pk)
    ctx = {"commission": commission_title, "comments": comments}
    return render(request, "commissions/commission_detail.html", ctx)
