# Generated by Django 3.2.7 on 2021-09-22 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0021_remove_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='details',
        ),
    ]
