from django.db import models

class Movie(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    text = models.CharField(verbose_name='Text', max_length=512)
    id_of_movie = models.CharField(verbose_name='Id of movie', max_length=128, unique=True)
    user = models.CharField(verbose_name='User login', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
