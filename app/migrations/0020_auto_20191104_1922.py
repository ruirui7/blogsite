# Generated by Django 2.1.7 on 2019-11-04 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20191104_1918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-updated']},
        ),
    ]
