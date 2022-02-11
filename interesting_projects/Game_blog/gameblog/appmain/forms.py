from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import password_changed
from . import models
from django.contrib.auth.forms import AuthenticationForm

class NewUserForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate', 'placeholder':'Login'}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'Email'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super().save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class AuthForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate', 'placeholder':'Login'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class ArticleForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title'}))
	text = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Text'}), max_length=2560)

	class Meta:
		model = models.Article
		fields = ['title', 'text', 'image', 'video']