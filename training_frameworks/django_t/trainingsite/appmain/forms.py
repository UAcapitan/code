from django import forms
from .models import *

class AddForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows':10}))
    is_published = forms.BooleanField()
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Empty')

