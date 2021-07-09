from django.forms.widgets import TextInput, Textarea
from .models import Article
from django.forms import ModelForm

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'text', 'author', 'image']

        widgets = {
            'name': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Name'
            }),
            'text': Textarea(attrs={
                'class':'form-control',
                'placeholder':'Text'
            }),
            'author': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Author'
            }),
            'image': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Image URL'
            })
        }