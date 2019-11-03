from django import forms
from .models import Genre, Category, Comment
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget
import datetime

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'