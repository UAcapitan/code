from django.db import models

class Articles(models.Model):
    create_date = models.DateTimeField(auto_now=True),
    name = models.CharField('name', max_length=50),
    text = models.TextField('text')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
