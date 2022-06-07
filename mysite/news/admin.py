from django.contrib import admin
from django.contrib.auth import forms
from django.forms.widgets import Widget
from .models import Post
from modeltranslation.admin import TranslationAdmin


class NewsCustomAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_ru')

    class Meta:
        verbose_name = "News"


class NewsAdmin(NewsCustomAdmin, TranslationAdmin):
    pass


admin.site.register(Post, NewsAdmin)