# Generated by Django 2.2.4 on 2019-08-30 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190830_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo_main',
        ),
    ]
