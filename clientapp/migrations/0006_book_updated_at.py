# Generated by Django 2.1.7 on 2020-04-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0005_auto_20200416_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
