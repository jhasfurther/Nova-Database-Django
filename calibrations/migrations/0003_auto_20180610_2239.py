# Generated by Django 2.0.6 on 2018-06-10 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibrations', '0002_auto_20180610_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibrations',
            name='pdf_of_Instructions',
            field=models.FileField(default=None, upload_to='media'),
        ),
    ]
