# Generated by Django 2.1.7 on 2019-10-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_comment_mes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='mes',
            field=models.CharField(default=1, max_length=255, verbose_name='題名'),
            preserve_default=False,
        ),
    ]
