from modeltranslation.translator import register, TranslationOptions
from .models import Post

@register(Post)
class PostTranslationsOptions(TranslationOptions):
    fields = ['title', 'body', 'detail']

# translator.register(Post, PostTranslationsOptions)

