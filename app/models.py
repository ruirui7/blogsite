from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

class Genre(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

class Category(models.Model):
	title = models.CharField('スレッド名', max_length=100)
	genre = models.ForeignKey(Genre, blank=True, null=True, on_delete=models.CASCADE)
	message = models.CharField('メッセ―ジ', max_length=255)
	author = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE)
	created_at = models.DateTimeField('作成日', default=timezone.now)
	updated_at = models.DateTimeField('更新日', default=timezone.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('app:detail', kwargs={'pk': self.pk})
		
class Comment(models.Model):
	comment = models.CharField('コメント', max_length=255)
	mes = models.CharField('題名', max_length=255)
	author = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE)
	created = models.DateTimeField('作成日', default=timezone.now)
	updated = models.DateTimeField('更新日', default= timezone.now)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.comment

	def get_absolute_url(self):
		return reverse('app:come')



