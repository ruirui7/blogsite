# Generated by Django 2.1.7 on 2020-04-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20200408_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=1000, verbose_name='コメント'),
        ),
    ]
