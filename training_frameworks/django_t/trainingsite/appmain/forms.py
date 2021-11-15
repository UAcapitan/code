from django import forms
from .models import *
from django.core.exceptions import ValidationError

class AddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Empty'

    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'content': forms.Textarea(attrs={'cols':60, 'rows':10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Length more than 200 symbols')

        return title        

    def clean_content(self):
        text = self.cleaned_data['content']
        if len(text) < 5:
            raise ValidationError('Length less than 5 symbols')

        return text        

