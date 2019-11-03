from django.contrib import admin
from .models import Genre, Category, Comment

admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(Category)