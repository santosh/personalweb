from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default="default.jpg", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def get_snippet(self):
        return " ".join(str(self.body).split()[:20]) + "..."
