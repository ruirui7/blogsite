from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import ModelFormMixin
from .models import Category, Comment
from .forms import CommentForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class IndexView(generic.ListView):
	#template_name = 'app/index.html'
	model = Category
	def ind(request):
		context = { 'title': Category.objects.all(), }
		return render(request, 'app:category_list', context)
# def index(request):
# 		d = { 'title': Category.objects.all(), }
# 		return render(request, 'app/index.html', d)

class DetailView(ModelFormMixin, generic.DetailView):
	model = Category
	form_class = CommentForm

	def get_context_data(self, *wargs, **kwargs):
		context = super().get_context_data(**kwargs)
		context.update({
			'comments': Comment.objects.filter(category=self.object),
			})

		return context
	def form_valid(self, form):
		comment = form.save(commit=False)#instance
		comment.category = self.get_object()
		comment.author = self.request.user#.groupもできる
		comment.save()
		return redirect('app:detail', pk=self.get_object().id)


	# fields = ['comment']
	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid(): #and get_object_or_404(User, pk=request.user.id):
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
	# def de(request):
	# 	context = { 'comments': Category.objects.all().order_by('id'), }
	# 	return render(request, 'app:category_detail', context)

	# def thr(request):
	# 	context = { 'title': Category.objects.all(), }
	# 	return render(request, 'app:category_detail', context)

	# template_name = 'app/thread.html'
	# def thr(request):
	# 	context = { 'title': Category.objects.all(), }
	# 	return render(request, 'app/thread.html', context)

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
	model = Category
	fields = ['title', 'genre', 'created_at']


class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
	model = Category
	fields = ['title', 'genre', 'updated_at']#'__all__'

	# def dispatch(self, request, *args, **kwargs):←ユーザーを定義したら復活
	# 	obj = self.get_object()
	# 	if obj.author != self.request.user:
	# 		raise PermissionDenied('You do not have permission to edit.')
	# 	return super(UpdateView, self).dispatch(request, *args, **kwargs)

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
	model = Category
	success_url = reverse_lazy('app:index')




class ComeView(generic.ListView):
    template_name = 'app/comment.html'
    model = Comment
    # form_class = CommentForm
    # date_field = 'comment'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
    def come_list(request):
        context = { 'comment': Comment.objects.all(), }
        return render(request, 'app:comment', context)

class ComeDetailView(ModelFormMixin, generic.DetailView):
	template_name = 'app/comment_detail.html'
	model = Category
	form_class = CommentForm


	# fields = ['comment']
	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.isvalid() and get_object_or_404(User, pk=request.user.id):
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

class ComeCreateView(generic.CreateView):
    template_name = 'app/comment_create.html'
    model = Comment
    fields = ['comment']

class ComeDeleteView(generic.DeleteView):
    template_name = 'app/comment_delete.html'
    model = Comment
    fields = ['comment']
