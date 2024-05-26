# Generated by Django 5.0.4 on 2024-05-12 21:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0015_projects_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='longitude',
        ),
        migrations.AddField(
            model_name='projects',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='map.area'),
        ),
    ]