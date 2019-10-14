from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Category

class IndexView(generic.ListView):
	template_name = 'app/index.html'
	model = Category