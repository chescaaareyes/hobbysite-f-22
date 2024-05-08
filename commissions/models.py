from django.db import models
from django.db.models import Case, Value, When
from django.urls import reverse

from user_management.models import Profile


class Commission(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="commission", default=1
    )
    description = models.TextField()
    STATUS_CHOICES = {
        "Open": "Open",
        "Full": "Full",
        "Completed": "Completed",
        "Discontinued": "Discontinued",
    }
    status = models.CharField(max_length=14, choices=STATUS_CHOICES, default="Open")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("commissions:commission_detail", args=[self.pk])

    def get_jobs(self):
        return Job.objects.filter(commission__pk=self.pk)

    class Meta:
        ordering = ["created_on"]


class Job(models.Model):
    commission = models.ForeignKey(
        Commission, on_delete=models.CASCADE, related_name="job"
    )
    role = models.CharField(max_length=255)
    manpower = models.PositiveIntegerField()
    STATUS_CHOICES = {
        "Open": "Open",
        "Full": "Full",
    }
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default="Open")

    def __str__(self):
        return self.role

    def get_job_applications(self):
        return JobApplication.objects.filter(job__pk=self.pk)

    def get_number_of_accepted_applications(self):
        return (
            JobApplication.objects.filter(job__pk=self.pk)
            .filter(status="Accepted")
            .count()
        )

    class Meta:
        ordering = [
            Case(
                When(status="Open", then=Value(0)),
                When(status="Full", then=Value(1)),
            ),
            "-manpower",
            "role",
        ]


class JobApplication(models.Model):
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name="job_application", editable=False
    )
    applicant = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="job_application"
    )
    STATUS_CHOICES = {
        "Pending": "Pending",
        "Accepted": "Accepted",
        "Rejected": "Rejected",
    }
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="Pending")
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            Case(
                When(status="Pending", then=Value(0)),
                When(status="Accepted", then=Value(1)),
                When(status="Rejected", then=Value(2)),
            ),
            "-applied_on",
        ]
