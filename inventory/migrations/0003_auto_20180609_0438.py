# Generated by Django 2.0.6 on 2018-06-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20180609_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='Due_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='Equipment_List',
            field=models.CharField(choices=[('Tool', 'TL'), ('BARBA', 'BA'), ('Sieve', 'SV'), ('Compaction Mold', 'CM'), ('Cool dude', 'CS'), ('Soundness Sieve', 'SS'), ('Marshall Apparatus', 'MA')], default=None, max_length=256),
        ),
    ]