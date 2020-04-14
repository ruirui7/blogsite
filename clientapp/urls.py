from django.urls import path
from . import views

app_name = 'clientapp'

urlpatterns = [
    path('', views.ClientIndexView.as_view(), name='index'),
    path('<int:pk>/client_detail', views.ClientDetailView.as_view(), name='client_detail'),
    path('client_create/', views.ClientCreateView.as_view(), name='client_create'),
    path('<int:pk>/client_update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('<int:pk>/client_delete/', views.ClientDeleteView.as_view(), name='client_delete'),
]
