from django.db import models
from django.urls import reverse


class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("forum:forum_list", args=[self.pk])

    class Meta:
        ordering = ["name"]


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        PostCategory, on_delete=models.SET_NULL, related_name="categories", null=True
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
