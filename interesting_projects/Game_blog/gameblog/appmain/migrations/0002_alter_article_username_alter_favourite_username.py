# Generated by Django 4.0 on 2022-01-27 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='username',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='favourite',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
