# Generated by Django 2.0.6 on 2018-08-04 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0023_auto_20180804_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='pdf_1',
            field=models.FileField(blank=True, default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='pdf_2',
            field=models.FileField(blank=True, default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='pdf_3',
            field=models.FileField(blank=True, default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='pdf_4',
            field=models.FileField(blank=True, default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='pdf_5',
            field=models.FileField(blank=True, default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='pdf_6',
            field=models.FileField(blank=True, default=None, upload_to=''),
        ),
    ]