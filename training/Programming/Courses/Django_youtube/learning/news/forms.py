
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from . import models


class ArticleForm(ModelForm):
    class Meta:
        model = models.Articles
        fields = ["title", "author", "full_text", "date"]

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title"
            }),
            "author": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Author"
            }),
            "full_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Text"
            }),
            "date": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Date of publication"
            })
        }