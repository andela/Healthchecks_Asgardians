# coding: utf-8

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ("design", "Design"),
    ("programming", "Programming"),
    ("new_technologies", "New Technologies"),
    ("ui/ux", "UI/UX"),
    ("cronjobs", "Cron_jobs"),
    ("others", "Others")
)


class Post(models.Model):
    author = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES)
    content = models.TextField()
    published_date = models.DateTimeField(null=True, blank=True,
                                          editable=False)

    def __str__(self):
        return self.title

    def published_date(self):
        self.published_date = timezone.now()
        self.save()
