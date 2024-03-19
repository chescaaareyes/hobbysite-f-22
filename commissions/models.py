from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Commission(models.Model):
    title = models.CharField(max_length=255, default="this")
    desc = models.TextField(default="this")
    people_required = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("commissions:commission", args=[self.pk])


class Comment(models.Model):
    commission = models.ForeignKey(
        Commission, on_delete=models.CASCADE, related_name="commissions"
    )
    entry = models.TextField(default="this")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
