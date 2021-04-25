from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class Task_form(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),

            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text'
            })
        }