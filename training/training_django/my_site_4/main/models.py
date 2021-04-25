from django.db import models

class Article(models.Model):
    article_name = models.CharField(max_length=50)
    text = models.TextField('text')
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article_name

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'