from django.db import models
from django.contrib.auth.models import User
from django.utils.translation.template import inline_re


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
