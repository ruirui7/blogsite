import datetime

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm
)
from django.contrib.auth import get_user_model

# from django.core.validators import FileExtensionValidator

class SignUpForm(UserCreationForm):
	# name = forms.CharField()
	email = forms.EmailField()
	# 年齢 = forms.IntegerField()
	# 性別 = forms.ChoiceField(choices=[
 #        ('item1', 'man'), ('item2', 'woman')
 #    ])
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')