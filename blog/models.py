from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(
        Category, related_name="content", on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(Tags, related_name="content")
    body = models.TextField()
    publish = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="content",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

