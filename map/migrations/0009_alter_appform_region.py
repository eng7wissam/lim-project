# Generated by Django 5.0.4 on 2024-05-09 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_appform_region_alter_appform_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appform',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.regions'),
        ),
    ]
