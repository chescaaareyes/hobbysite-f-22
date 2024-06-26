import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Case, Sum, Value, When
from django.shortcuts import redirect, render

from user_management.models import Profile

from .forms import CommissionForm, JobApplicationForm, JobFormSet
from .models import Commission, Job, JobApplication


def commission_list(request):
    all_commissions = Commission.objects.annotate(
        custom_order=Case(
            When(status="Open", then=Value(0)),
            When(status="Full", then=Value(1)),
            When(status="Completed", then=Value(2)),
            When(status="Discontinued", then=Value(3)),
        )
    ).order_by("custom_order")
    if request.user.is_authenticated:
        created_commissions = Commission.objects.filter(author__user=request.user)
        applied_commissions = Commission.objects.filter(
            job__job_application__applicant__user=request.user
        ).distinct()
    else:
        created_commissions = None
        applied_commissions = None
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

    application_form = None

    if request.user.is_authenticated:
        application_form = JobApplicationForm(
            initial={
                "job": Job.objects.get(pk=1),
                "applicant": Profile.objects.get(user=request.user),
                "status": "Pending",
            }
        )
        if request.method == "POST":
            application_form = JobApplicationForm(request.POST)
            if application_form.is_valid():
                new_application = JobApplication()
                job_pk = int(request.POST.get("job-pk"))
                new_application.job = Job.objects.get(pk=job_pk)
                new_application.applicant = Profile.objects.get(user=request.user)
                new_application.status = "Pending"
                new_application.save()
                return redirect("commissions:commission_detail", pk=pk)

    ctx = {
        "commission": commission,
        "jobs": jobs,
        "manpower_required": manpower_required,
        "manpower_open": manpower_open,
        "application_form": application_form,
    }

    return render(request, "commissions/commission_detail.html", ctx)


@login_required
def commission_create(request):
    author = Profile.objects.get(user=request.user)
    commission_form = CommissionForm(initial={"author": author})
    job_form = JobFormSet()
    if request.method == "POST":
        commission_form = CommissionForm(request.POST)
        job_form = JobFormSet(request.POST)
        if commission_form.is_valid() and job_form.is_valid():
            # for commission
            new_commission = Commission()
            new_commission.title = commission_form.cleaned_data.get("title")
            new_commission.description = commission_form.cleaned_data.get("description")
            new_commission.status = commission_form.cleaned_data.get("status")
            new_commission.author = author
            new_commission.save()
            # for job
            for form in job_form:
                new_job = Job()
                new_job.commission = Commission.objects.get(pk=new_commission.pk)
                new_job.role = form.cleaned_data.get("role")
                new_job.manpower = form.cleaned_data.get("manpower")
                new_job.status = form.cleaned_data.get("status")
                new_job.save()
            return redirect("commissions:commission_detail", pk=new_commission.pk)
    new_created_on = datetime.datetime.now()
    new_updated_on = datetime.datetime.now()
    ctx = {
        "commission_form": commission_form,
        "job_form": job_form,
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
    form = CommissionForm(
        initial={
            "title": commission.title,
            "description": commission.description,
            "status": current_status,
            "author": commission.author,
        }
    )
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
