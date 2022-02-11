from django.contrib import admin
from . import models

admin.site.register(models.Article)
admin.site.register(models.Favourite)
admin.site.register(models.Recommendation)
admin.site.register(models.Comments)