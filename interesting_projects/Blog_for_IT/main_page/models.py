from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    image = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Avatar(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.image

    class Meta:
        verbose_name = 'Avatar'
        verbose_name_plural = 'Avatars'