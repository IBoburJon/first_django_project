from django import forms  
from news.models import Post  

class NewsForm(forms.ModelForm):  
    class Meta:  
        model = Post 
        fields = ['title', 'body', 'detail']
          