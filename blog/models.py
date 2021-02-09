from django.db import models
from django.contrib.auth.models import User

class Feed(models.Model):
    feed_link = models.CharField(max_length=2000, blank=True)
    link = models.CharField(max_length=2000)
    title = models.TextField()
    desc = models.TextField()
    favourite = models.ManyToManyField(User, related_name='feeds', blank=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    link = models.CharField(max_length=2000)
    title = models.TextField()
    desc = models.TextField()
