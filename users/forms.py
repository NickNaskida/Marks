from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=50)

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
