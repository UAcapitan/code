from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Name')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null='True')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'id': self.pk})

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-title', 'id']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'id': self.pk})