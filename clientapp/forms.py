from django import forms
from .models import Client,Book
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget
# from django.core.validators import FileExtensionValidator
import datetime

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('__all__')#'org','scale','proposals', 'mat_trend','mat_total',
        	#'priority','memo','author','created_at','updated_at'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class BookForm(forms.ModelForm):
	# image = forms.ImageField()

	class Meta:
		model = Book
		fields = ('__all__')
