# Generated by Django 2.1.7 on 2020-04-14 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0002_client_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterField(
            model_name='client',
            name='memo',
            field=models.TextField(max_length=1000, verbose_name='詳細メモ'),
        ),
    ]
