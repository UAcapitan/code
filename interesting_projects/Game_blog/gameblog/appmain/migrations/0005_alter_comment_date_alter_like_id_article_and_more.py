# Generated by Django 4.0 on 2022-02-11 17:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('appmain', '0004_comment_rename_favourite_like_alter_like_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 11, 19, 33, 26, 509809)),
        ),
        migrations.AlterField(
            model_name='like',
            name='id_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appmain.article'),
        ),
        migrations.AlterField(
            model_name='like',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
