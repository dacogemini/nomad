from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Highlight(models.Model):
    title = models.CharField(max_length=200, unique=True)
    details = models.CharField(null=True, max_length=200)
    description = models.TextField(blank=True)
    trip_id = models.URLField(max_length=128, db_index=True,
                              blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, default=True, unique=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
