from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article
from captcha.fields import CaptchaField
class UserRegistrationForm(UserCreationForm):
	email=forms.EmailField()
	captcha=CaptchaField()
	class Meta:
		model=User
		fields=['username','email','password1','password2']
class ArticleForm(forms.ModelForm):
	class Meta():
		model=Article
		fields=['title','Description',"Image"]