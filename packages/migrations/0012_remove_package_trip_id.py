# Generated by Django 2.0.2 on 2019-08-09 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0011_auto_20190809_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='trip_id',
        ),
    ]
