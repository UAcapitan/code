from django.db import models


class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    author = models.CharField('Author', max_length=50)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date of publication')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"