# Generated by Django 3.2.7 on 2021-09-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0029_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='detail_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='detail_ru',
            field=models.TextField(blank=True, null=True),
        ),
    ]
