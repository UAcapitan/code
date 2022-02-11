import datetime
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    username = models.CharField(max_length=50)
    date_of_save = models.DateField(default=datetime.date.today()) 
    image = models.ImageField(upload_to='articles/')
    video = models.CharField(max_length=512)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Favourite(models.Model):
    username = models.CharField(max_length=50)
    id_article = models.IntegerField()

    def __str__(self):
        return self.id_article

    class Meta:
        verbose_name = 'Favourite'
        verbose_name_plural = 'Favourites'

class Recommendation(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = 'Recommendation'
        verbose_name_plural = 'Recommendations'

class Comments(models.Model):
    text = models.CharField(max_length=4096)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'