# Generated by Django 3.2.7 on 2021-09-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
