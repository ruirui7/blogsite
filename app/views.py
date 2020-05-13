import csv
import io
import pytz
import datetime

from django.contrib.auth.models import User
from .models import Category, Comment
from .forms import CommentForm# CSVUploadForm
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)
from .forms import MyPasswordChangeForm

from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views import generic
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import date

from django.db.models import Q


#-----------------------------------------
# ページネーション機能
#-----------------------------------------

def board(request, num=1):
    page = Paginator(Category.objects.all())
    params = {
            'login_user': request.user,
            'contents': page.get_page(num),
            'page': page.page_range,
            'page_active': num,
            'page_last': page.num_pages,
        }
    return render(request, 'app/board.html', params)

# def com_board(request, num=1):
# 	page = Paginator(Comment.objects.all())
# 	params = {
#             'login_user': request.user,
#             'contents': page.get_page(num),
#             'page': page.page_range,
#             'page_active': num,
#             'page_last': page.num_pages,
#         }
# 	return render(request, 'app/comment_board.html', params)

#-----------------------------------------
# カテゴリー項目
#-----------------------------------------

class IndexView(generic.ListView):
    model = Category
    queryset = Category.objects.order_by('-updated_at')
    paginate_by = 5
    # form_class = CommentForm

    def get_queryset(self, *args, **kwargs):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Category.objects.filter(
                Q(title__icontains=q_word)|Q(genre__name__icontains=q_word)|Q(message__icontains=q_word))
        else:
            object_list = Category.objects.all()
        return object_list

    # def get_context_data(self, *wargs, **kwargs):
    #     q_word = self.request.GET.get('query')
    #     context = super().get_context_data(**kwargs)
    #     if q_word:
    #          context.update({
    #             'client': Client.objects.filter(Q(client__icontains=q_word)),
    #             })
    #     else:
    #         context.update({
    #             'client': Client.objects.all(),
    #             })
    #     return context

class DetailView(ModelFormMixin, generic.DetailView):
	model = Category
	form_class = CommentForm

	def get_context_data(self, *wargs, **kwargs):
		q_word = self.request.GET.get('query')
		context = super().get_context_data(**kwargs)
		if q_word:
			 context.update({
			 	'comments': Comment.objects.filter(Q(mes__icontains=q_word)),
			 	})
		else:
			#時間をdatetime型からUTC表記に変換してUTC時間で日本時間へ適応させる。５日前までフィルターかけたものを表示させる。
			up_time = datetime.datetime.now().now(pytz.timezone('UTC')) - datetime.timedelta(days=5)
			up_time = up_time + datetime.timedelta(hours=9)
			context.update({
				'comments': Comment.objects.order_by('-updated').filter(category=self.object, updated__gt=up_time),
				# updated__gt=timezone.datetime.today()を入れるとworningになる。
				})
			paginate_by = 5
		return context

	def form_valid(self, form):
		comment = form.save(commit=False)
		comment.category = self.get_object()
		comment.author = self.request.user
		comment.save()
		
		return redirect('app:detail', pk=self.get_object().id)

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
	model = Category
	fields = ['title', 'genre', 'message','memo' ,'author']

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
	model = Category
	fields = ['title', 'genre', 'message', 'memo' ,'author']#'updated_at'#'__all__'

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
	model = Category
	success_url = reverse_lazy('app:index')

#-----------------------------------------
# コメント項目
#-----------------------------------------

#今のところUPDATEだけで十分
class ComeUpdateView(generic.UpdateView):
    template_name = 'app/comment_form.html'
    model = Comment
    form_class = CommentForm

# class ComeView(generic.ListView):
#     template_name = 'app/comment.html'
#     model = Comment

#     def come_list(request):
#         context = { 'comment': Comment.objects.all(), }
#         return render(request, 'app:comment', context)

# class ComeDetailView(generic.DetailView):
# 	template_name = 'app/comment_detail.html'
# 	model = Comment
# 	form_class = CommentForm

# 	def post(self, request, *args, **kwargs):
# 		form = self.get_form()
# 		if form.isvalid() and get_object_or_404(User, pk=request.user.id):
# 			return self.form_valid(form)
# 		else:
# 			return self.form_invalid(form)

#-----------------------------------------
# CSVダウンロード項目
#-----------------------------------------

class CSVIndexView(generic.ListView):
    template_name = 'app/CSV.html'
    model = Category

def category_export(request):
    response = HttpResponse(content_type='text/csv')
    t = date.today() - datetime.timedelta(days=1)
    file_name = t.strftime('%Y%m') + '_CSV.csv'
    response['Content-Disposition'] = 'attachment; filename="SE_LIST"' + file_name
    response_file = io.TextIOWrapper(response, encoding='cp932')
    writer = csv.writer(response_file)
    to_month_date = timezone.now()
    start_date = datetime.datetime.now().now(pytz.timezone('UTC')).replace(day=1) - relativedelta(months=1)#前月分１日取得
    end_date = datetime.datetime.now().now(pytz.timezone('UTC')).replace(day=1) - datetime.timedelta(days=1)#前月分最終日取得
    order_list = Category.objects.filter(updated_at__gte=start_date).filter(updated_at__lte=end_date)
    for category in order_list:
        writer.writerow([
        	category.pk,
        	category.title,
        	category.genre,
        	category.author,
        	category.created_at,
        	category.updated_at,
        	])
    return response

def comment_export(request):
    response = HttpResponse(content_type='text/csv')
    t = date.today() - relativedelta(months=1)
    file_name = t.strftime('%Y%m') + '_CSV.csv'
    response['Content-Disposition'] = 'attachment; filename="SE_MATLIST"' + file_name
    response_file = io.TextIOWrapper(response, encoding='cp932')
    writer = csv.writer(response_file)

    start_date = datetime.datetime.now().now(pytz.timezone('UTC')).replace(day=1) - relativedelta(months=1)#前月分１日取得
    end_date = datetime.datetime.now().now(pytz.timezone('UTC')).replace(day=1) - datetime.timedelta(days=1)#前月分最終日取得
    order_list = Comment.objects.filter(updated__gte=start_date).filter(updated__lte=end_date)
    for comment in order_list:
        writer.writerow([
        	comment.pk,
        	comment.comment,
        	comment.mes,
        	comment.author,
        	comment.created,
        	comment.updated,
        	])
    return response

#-----------------------------------------
# パスワード変更項目
#-----------------------------------------

class PasswordChange(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('app:password_change_done')
    template_name = 'app/password_change.html'


class PasswordChangeDone(PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = 'app/password_change_done.html'

#-----------------------------------------
# マイページ項目
#-----------------------------------------

class MypageView(generic.ListView):
    template_name = 'app/mypage.html'
    model = User
    #ユーザーはそのまま使える気がする。{{user.username}}
    #modelを別のクラスにして取得してUSERクラスはそのまま引っ張ればいけそう。