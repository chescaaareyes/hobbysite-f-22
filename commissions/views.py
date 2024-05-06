import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Case, Sum, Value, When
from django.shortcuts import redirect, render

from .forms import CommissionForm, JobApplicationForm
from .models import Commission, Job
from user_management.models import Profile


def commission_list(request):
    all_commissions = Commission.objects.annotate(
        custom_order=Case(
            When(status="Open", then=Value(0)),
            When(status="Full", then=Value(1)),
            When(status="Completed", then=Value(2)),
            When(status="Discontinued", then=Value(3)),
        )
    ).order_by("custom_order")
    created_commissions = Commission.objects.filter(author__user__pk=request.user.pk)
    applied_commissions = Commission.objects.filter(
        job__job_application__applicant__user__pk=request.user.pk
    )
    ctx = {
        "all_commissions": all_commissions,
        "created_commissions": created_commissions,
        "applied_commissions": applied_commissions,
    }
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
    
    job_form = JobApplicationForm()
    if request.method == "POST":
        job_form = JobApplicationForm(request.POST)
        if job_form.is_valid():
            new_job = Job()
            new_job.job = job_form.cleaned_data.get("job")
            new_job.applicant = job_form.cleaned_data.get("applicant")
            new_job.status = "Pending"
            return redirect("commissions:commission_detail", pk=pk)

    ctx = {
        "commission": commission,
        "jobs": jobs,
        "manpower_required": manpower_required,
        "manpower_open": manpower_open,
        "job_form": job_form
    }

    return render(request, "commissions/commission_detail.html", ctx)


@login_required
def commission_create(request):
    author = Profile.objects.get(pk=request.user.pk)
    form = CommissionForm(initial={"author": author})
    if request.method == "POST":
        form = CommissionForm(request.POST)
        if form.is_valid():
            new_commission = Commission()
            new_commission.title = form.cleaned_data.get("title")
            new_commission.description = form.cleaned_data.get("description")
            new_commission.status = form.cleaned_data.get("status")
            new_commission.author = author
            new_commission.save()
            return redirect("commissions:commission_detail", pk=new_commission.pk)
    new_created_on = datetime.datetime.now()
    new_updated_on = datetime.datetime.now()
    ctx = {
        "form": form,
        "created_on": new_created_on,
        "updated_on": new_updated_on,
    }
    return render(request, "commissions/commission_create.html", ctx)


@login_required
def commission_update(request, pk):
    commission = Commission.objects.get(pk=pk)
    required_count = Job.objects.filter(commission__pk=pk).count()
    accepted_count = Job.objects.filter(commission__pk=pk).filter(status="Full").count()
    if accepted_count == required_count:
        current_status = "Full"
    else:
        current_status = commission.status
    form = CommissionForm(initial={"title": commission.title, "description": commission.description, "status": current_status, "author": commission.author})
    if request.method == "POST":
        form = CommissionForm(request.POST)
        if form.is_valid():
            commission.title = form.cleaned_data.get("title")
            commission.description = form.cleaned_data.get("description")
            commission.status = current_status
            commission.updated_on = datetime.datetime.now()
            commission.save()
            return redirect("commissions:commission_detail", pk=commission.pk)
    new_updated_on = datetime.datetime.now()
    ctx = {"form": form, "commission": commission, "updated_on": new_updated_on}
    return render(request, "commissions/commission_update.html", ctx)
