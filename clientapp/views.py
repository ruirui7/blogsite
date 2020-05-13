from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Client,Book
from .forms import ClientForm,BookForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views import generic

from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import date

from django.db.models import Q
from django.conf import settings

#-----------------------------------------
# 顧客リスト項目
#-----------------------------------------

class ClientIndexView(generic.ListView):
	template_name = 'clientapp/index.html'
	model = Client
	queryset = Client.objects.order_by('-updated_at')
	paginate_by = 5

	def get_queryset(self, *args, **kwargs):
		q_word = self.request.GET.get('query')
		if q_word:
			object_list = Client.objects.filter(
				Q(name__icontains=q_word)|
				Q(org__icontains=q_word)|
				Q(scale__icontains=q_word)|
				Q(mat_trend__icontains=q_word)|
				Q(mat_total__icontains=q_word)|
				# Q(author__icontains=q_word)|
				Q(priority__icontains=q_word)
				)
		else:
			object_list = Client.objects.all()
		return object_list

class ClientDetailView(generic.DetailView):
	template_name = 'clientapp/detail.html'
	model = Client

	def get_context_data(self, *wargs, **kwargs):
		context = super().get_context_data(**kwargs)
		context.update({
			'client': Client.objects.filter(name=self.object)
			})
		return context

class ClientCreateView(LoginRequiredMixin, generic.edit.CreateView):
	template_name = 'clientapp/client_form.html'
	model = Client
	fields = ['name','org','scale','proposals', 'mat_trend','mat_total','priority','memo','author']

class ClientUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
	template_name = 'clientapp/client_form.html'
	model = Client
	fields = ['name','org','scale','proposals', 'mat_trend','mat_total','priority','memo','author']

class ClientDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
	template_name = 'clientapp/delete.html'
	model = Client
	success_url = reverse_lazy('clientapp:index')

#-----------------------------------------
# 写真アップロード項目
#-----------------------------------------

class FiileListView(generic.ListView):
	"""ファイル一覧ビュー"""
	template_name = 'clientapp/file_list.html'
	model = Book
	# form_class = BookForm

class FiileCreateView(generic.CreateView):
    """ファイルモデルのクリエイトビュー"""
    model = Book
    fields = ["image"]
    template_name = 'clientapp/file_form.html'
    success_url = reverse_lazy('clientapp:file_list')

class FiileUpdateView(generic.UpdateView):
	"""ファイルモデルのアップデートビュー"""
	template_name = 'clientapp/file_form.html'
	model = Book
	fields = ["image"]
	def my_view(request):
		if foo:
			return HttpResponseNotFound('<h1>Page not found</h1>')
		else:
			return HttpResponse('<h1>Page was found</h1>')

class FiileDeleteView(generic.DeleteView):
	"""ファイルモデルのデリートビュー"""
	template_name = 'clientapp/file_delete.html'
	model = Book
	fields = ["__all__"]
	success_url = reverse_lazy('clientapp:file_list')