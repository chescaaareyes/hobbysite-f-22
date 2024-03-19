from django.shortcuts import render

from .models import Comment, Commission


def commissions_list(request):
    commissions = Commission.objects.all().order_by("created_on")
    ctx = {"commissions": commissions}
    return render(request, "commissions/commissions_list.html", ctx)


def commission(request, pk):
    commission_title = Commission.objects.get(pk=pk)
    comments = Comment.objects.filter(commission__pk=pk).order_by("created_on")
    ctx = {"commission": commission_title, "comments": comments}
    return render(request, "commissions/commission.html", ctx)
