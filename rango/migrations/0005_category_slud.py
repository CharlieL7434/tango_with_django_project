# Generated by Django 2.2.3 on 2020-02-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20200207_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slud',
            field=models.SlugField(default='1'),
            preserve_default=False,
        ),
    ]
