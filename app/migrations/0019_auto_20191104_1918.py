# Generated by Django 2.1.7 on 2019-11-04 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20191103_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-updated_at']},
        ),
    ]