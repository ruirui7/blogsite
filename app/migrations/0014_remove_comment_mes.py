# Generated by Django 2.1.7 on 2019-10-23 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20191024_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='mes',
        ),
    ]
