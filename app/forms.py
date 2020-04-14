from django import forms
from .models import Genre, Category, Comment
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget

from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm
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