from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

class Genre(modesls.Model):
	name = models.CharField(max_length=100)


class Category(models.Model):
	title = models.CharField('スレッド名',max_length=100)
	genre = models.ForeignKey(Genre, blank=True, null=True, on_delete=models.CASCADE)
	author = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    updated_at = models.DateTimeField('更新日', default=timezone.now)