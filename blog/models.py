from django.db import models
from django.contrib.auth.models import User

class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=2000)
    title = models.TextField()
    desc = models.TextField()

class Article(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    link = models.CharField(max_length=2000)
    title = models.TextField()
    desc = models.TextField()