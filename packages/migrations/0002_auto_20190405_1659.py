# Generated by Django 2.0.2 on 2019-04-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]
