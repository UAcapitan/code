from django import forms

class ArticleFrom(forms.Form):
    name = forms.CharField(max_length=100)
    text = forms.CharField(max_length=900)
    author = forms.CharField(max_length=50)
    image = forms.CharField(max_length=200, default='')