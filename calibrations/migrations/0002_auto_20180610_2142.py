# Generated by Django 2.0.6 on 2018-06-10 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibrations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calibrations',
            name='Type_of_Calibration',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='calibrations',
            name='pdf_of_Instructions',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
