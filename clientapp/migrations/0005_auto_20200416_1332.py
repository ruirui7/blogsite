# Generated by Django 2.1.7 on 2020-04-16 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0004_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='link',
        ),
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
