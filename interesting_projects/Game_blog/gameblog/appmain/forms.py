from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super().save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user 

# class ArticleForm(forms.Form):
# 	title = forms.CharField(label='Title', max_length=100)
# 	text = forms.CharField(label='Text', max_length=2560)

class ArticleForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title'}))
	text = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Text'}), max_length=2560)
	date_of_save = forms.DateField(input_formats=['%d-%m-%Y'], widget=forms.DateInput(attrs={'placeholder':'DD-MM-YYYY'}))

	class Meta:
		model = models.Article
		fields = ['title', 'text', 'date_of_save']