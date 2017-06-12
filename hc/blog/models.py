# coding: utf-8

from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    author = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=30)
    content = models.TextField()
    published_date = models.DateTimeField(null=True, blank=True,
                                          editable=False)

    def __str__(self):
        return self.title
