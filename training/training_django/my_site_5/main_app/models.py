from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
