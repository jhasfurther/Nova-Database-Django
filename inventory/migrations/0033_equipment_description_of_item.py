# Generated by Django 2.0.6 on 2018-08-08 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0032_remove_equipment_description_of_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='Description_of_Item',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
