from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm


#-----------------------------------------
# サインアップ項目
#-----------------------------------------

#元のサインアップフォーム
# class SignUpView(generic.CreateView):
# 	form_class = UserCreationForm
# 	success_url = reverse_lazy('login')
# 	template_name = 'accounts/signup.html'

class SignUpView(generic.CreateView):
	form_class = SignUpForm
	success_url = reverse_lazy('app:index')
	template_name = 'accounts/signup.html'