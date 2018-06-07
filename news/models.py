import datetime
from django.db import models
from django.utils import timezone

class Source(models.Model):
    source_name = models.CharField(max_length=200)
    source_url = models.URLField(unique=True, max_length=40)
    def __str__(self):
        return self.source_name

class Post(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)
    post_summary = models.CharField(max_length=200)
    post_detail = models.TextField(max_length=10000)
    post_url = models.URLField(max_length=100, default=None)
    created_at = models.DateTimeField('date published')

    def __str__(self):
        return self.post_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now
