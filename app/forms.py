from django import forms
from .models import Genre, Category, Comment
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget

from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm
)
from django.contrib.auth import get_user_model

# from django.core.validators import FileExtensionValidator
import datetime

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('mes', 'comment', 'author', 'updated')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class MyPasswordChangeForm(PasswordChangeForm):
    """パスワード変更フォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'



# class SignUpForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')


# class SignUpForm(UserCreationForm):
#     last_name = forms.CharField(
#         max_length=30,
#         required=False,
#         help_text='オプション',
#         label='苗字'
#     )
#     first_name = forms.CharField(
#         max_length=30,
#         required=False,
#         help_text='オプション',
#         label='名前'
#     )
#     email = forms.EmailField(
#         max_length=254,
#         help_text='必須 有効なメールアドレスを入力してください。',
#         label='Eメールアドレス'
#     )

#     class Meta:
#         model = User
#         fields = ('username', 'last_name', 'first_name',  'email', 'password1', 'password2', )