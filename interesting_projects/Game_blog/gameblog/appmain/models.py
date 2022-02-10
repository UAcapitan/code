import datetime
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    username = models.CharField(max_length=50)
    date_of_save = models.DateField(default=datetime.date.today()) 

    def __str__(self):
        return self.title

class Favourite(models.Model):
    username = models.CharField(max_length=50)
    id_article = models.IntegerField()

    def __str__(self):
        return self.id_article

class Recommendation(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.article.title