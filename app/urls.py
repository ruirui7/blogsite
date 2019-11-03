from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('create/', views.CreateView.as_view(), name='create'),
	path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
	path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),

	# path('<int:pk>/come/', views.ComeView.as_view(), name='come'),
 #    path('<int:pk>/come/', views.ComeDetailView.as_view(), name='comedetail'),
 #    path('comecreate/', views.ComeCreateView.as_view(), name='comecreate'), 
 #    path('<int:pk>/comedelete/', views.ComeDeleteView.as_view(), name='comedelete'),   
    #path('', views.index, name='index'),
    #path(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #path('thread/', views.thread, name='thread'),
    #path('index/', views.index, name='index'),
]
