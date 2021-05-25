from django import forms

class ArticleForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    text = forms.CharField(label='Text', max_length=255)
    user_name = forms.CharField(label='User name', max_length=50)