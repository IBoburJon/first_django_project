# Generated by Django 3.2.7 on 2021-09-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20210919_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_en',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_ru',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]