from . import models
from django.forms import IntegerField, ModelForm, NumberInput, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = models.Task
        fields = ["title", "task", "mark"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title"
            }),
            "task": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description"
            }),
            "mark": NumberInput(attrs={
                "class": "form-control"
            })
        }