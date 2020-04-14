from django.db import models
from django.utils import timezone
from django.urls import reverse

class Client(models.Model):
	name = models.CharField('名前', max_length=50)
	org = models.CharField('会社名', max_length=100)
	scale = models.CharField('人数規模', max_length=100)
	proposals = models.CharField('提案数', max_length=100)
	mat_trend = models.CharField('案件傾向', max_length=100)
	mat_total = models.CharField('案件総数', max_length=100)
	priority = models.CharField('優先度', max_length=100)
	memo = models.TextField('詳細メモ', max_length=1000)
	author = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE)
	created_at = models.DateTimeField('作成日', default=timezone.now)
	updated_at = models.DateTimeField('更新日', auto_now=True)

	class Meta:
		ordering = ['-updated_at']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('clientapp:client_detail', kwargs={'pk': self.pk})