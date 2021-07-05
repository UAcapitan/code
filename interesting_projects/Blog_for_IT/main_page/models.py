from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)