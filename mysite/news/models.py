from django.db import models
from django.db.models.fields import DateTimeField
from django.urls.base import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "post"

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender=Post)