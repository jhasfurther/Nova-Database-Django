# Generated by Django 2.0.6 on 2018-08-05 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calibrations', '0004_auto_20180805_0357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calibrations',
            name='test',
        ),
    ]
