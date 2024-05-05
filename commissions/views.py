from django.db.models import Case, Sum, Value, When
from django.shortcuts import render

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
