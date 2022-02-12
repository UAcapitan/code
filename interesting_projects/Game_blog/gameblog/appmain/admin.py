from django.contrib import admin
from . import models

admin.site.register(models.Article)
admin.site.register(models.Like)
admin.site.register(models.Recommendation)
admin.site.register(models.Comment)
admin.site.register(models.Avatar)