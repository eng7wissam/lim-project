# Generated by Django 5.0.4 on 2024-05-14 09:46

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0017_projects_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPointField(null=True, srid=4326),
        ),
    ]
