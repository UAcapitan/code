from django.db.models.base import Model
from django.forms.widgets import TextInput, Textarea
from .models import Article, Avatar
from django.forms import ModelForm
from django.contrib.auth.models import User

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
                'class':'form-control d-lg-none',
                'placeholder':'Author',
            }),
            'image': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Image URL'
            })
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']