from django.db import models

class Genre(models.Model):
    name = models.CharField(verbose_name='name', max_length=128)
    user = models.CharField(verbose_name='user', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Ganres'

class Movie(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    text = models.CharField(verbose_name='Text', max_length=512)
    id_of_movie = models.CharField(verbose_name='Id of movie', max_length=128, unique=True)
    user = models.CharField(verbose_name='User login', max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='genre', related_name='genre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

class Review(models.Model):
    text = models.CharField(verbose_name='text', max_length=512)
    article = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='article', related_name='reviews')
    user = models.CharField(verbose_name='user', max_length=255)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'