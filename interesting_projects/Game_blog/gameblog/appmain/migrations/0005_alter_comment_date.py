# Generated by Django 4.0 on 2022-02-14 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0004_alter_article_date_of_save_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 14, 13, 53, 53, 658134)),
        ),
    ]
