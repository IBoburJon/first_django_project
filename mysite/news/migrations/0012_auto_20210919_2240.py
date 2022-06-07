# Generated by Django 3.2.7 on 2021-09-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body_ru',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
