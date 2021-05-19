import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('name article', max_length=200)
    article_text = models.TextField('text article')
    pub_date = models.DateTimeField('date publication')
    def __str__(self):
        return self.article_title
    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('name author', max_length=50)
    comment_text = models.CharField('comment text', max_length=200)
    def __str__(self):
        return self.author_name