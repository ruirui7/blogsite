# Generated by Django 2.1.7 on 2020-04-08 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20200408_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日'),
        ),
    ]