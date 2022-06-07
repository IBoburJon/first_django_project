# Generated by Django 3.2.7 on 2021-09-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=250, null=True),
        ),
    ]