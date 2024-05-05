import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Case, Sum, Value, When
from django.shortcuts import redirect, render

from .forms import CommissionForm
from .models import Commission, Job


def commission_list(request):
    commissions = Commission.objects.annotate(
        custom_order=Case(
            When(status="Open", then=Value(0)),
            When(status="Full", then=Value(1)),
            When(status="Completed", then=Value(2)),
            When(status="Discontinued", then=Value(3)),
        )
    ).order_by("custom_order")
    ctx = {"commissions": commissions}
    return render(request, "commissions/commission_list.html", ctx)


def commission_detail(request, pk):
    commission = Commission.objects.get(pk=pk)
    jobs = Job.objects.filter(commission__pk=pk)

    if jobs:
        manpower_required = jobs.aggregate(manpower_sum=Sum("manpower"))["manpower_sum"]
    else:
        manpower_required = 0
    manpower_open = 0
    manpower_full = 0

    for job in jobs:
        job_applications = job.job_application.all()
        manpower_full += job_applications.filter(status="Accepted").count()

    manpower_open = manpower_required - manpower_full

    ctx = {
        "commission": commission,
        "jobs": jobs,
        "manpower_required": manpower_required,
        "manpower_open": manpower_open,
    }

    return render(request, "commissions/commission_detail.html", ctx)


@login_required
def commission_create(request):
    form = CommissionForm()
    if request.method == "POST":
        form = CommissionForm(request.POST)
        if form.is_valid():
            new_commission = Commission()
            new_commission.title = form.cleaned_data.get("title")
            new_commission.description = form.cleaned_data.get("description")
            new_commission.status = form.cleaned_data.get("status")
            new_commission.save()
            return redirect("commissions:commission_detail", pk=new_commission.pk)
    new_created_on = datetime.datetime.now()
    new_updated_on = datetime.datetime.now()
    ctx = {
        "form": form,
        "created_on": new_created_on,
        "updated_on": new_updated_on,
        "author": request.user,
    }
    return render(request, "commissions/commission_create.html", ctx)


@login_required
def commission_update(request, pk):
    commission = Commission.objects.get(pk=pk)
    form = CommissionForm()
    if request.method == "POST":
        form = CommissionForm(request.POST)
        if form.is_valid():
            commission.title = form.cleaned_data.get("title")
            commission.description = form.cleaned_data.get("description")
            commission.status = form.cleaned_data.get("status")
            commission.updated_on = datetime.datetime.now()
            commission.save()
            return redirect("commissions:commission_detail", pk=commission.pk)
    new_updated_on = datetime.datetime.now()
    ctx = {
        "form": form, "commission": commission, "updated_on": new_updated_on
    }
    return render(request, "commissions/commission_update.html", ctx)
