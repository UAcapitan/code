from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import password_changed
from . import models
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

class NewUserForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate', 'placeholder':'Login'}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'Email'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))

	captcha = CaptchaField()

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
	captcha = CaptchaField()

class ArticleForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title'}))
	text = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Text'}), max_length=2560)
	image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control form-control-sm'}))
	video = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'URL to video'}))

	class Meta:
		model = models.Article
		fields = ['title', 'text', 'image', 'video']

class CommentsForm(forms.ModelForm):
	text = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comment'}))

	class Meta:
		model = models.Comment
		fields = ['text', 'user', 'article']

class AvatarForm(forms.ModelForm):
	image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control form-control-sm'}))

	class Meta:
		model = models.Avatar
		fields = ['user','image']