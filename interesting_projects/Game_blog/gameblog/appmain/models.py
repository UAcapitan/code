from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    username = models.CharField(max_length=50)
    date_of_save = models.DateField()

    def __str__(self):
        return self.title

class Favourite(models.Model):
    username = models.CharField(max_length=50)
    id_article = models.IntegerField()

    def __str__(self):
        return self.id_article