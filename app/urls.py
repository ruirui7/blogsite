from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index', views.IndexView.as_view(), name='index_page'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/update2/', views.ComeUpdateView.as_view(), name='update2'),
	path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),

    path('board/', views.board, name='board'),
    # path('com_board/', views.com_board, name='com_board'),

    path('CSV', views.CSVIndexView.as_view(), name='CSV'),
    path('export/', views.category_export, name='export'),
    path('export_come/', views.comment_export, name='export_come'),

    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),

    path('Mypage', views.MypageView.as_view(), name='Mypage'),

]
