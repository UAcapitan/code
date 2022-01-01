from django.db import models
from django.forms import widgets

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_of_save = models.DateField()

    def __str__(self):
        return self.title
