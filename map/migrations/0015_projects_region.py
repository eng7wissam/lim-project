# Generated by Django 5.0.4 on 2024-05-11 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0014_remove_projects_activity_remove_projects_excutive_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='map.regions', verbose_name='ادخل المنطقة'),
            preserve_default=False,
        ),
    ]