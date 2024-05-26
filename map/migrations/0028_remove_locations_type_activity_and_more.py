# Generated by Django 5.0.4 on 2024-05-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0027_remove_projects_city_remove_projects_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locations',
            name='type_activity',
        ),
        migrations.AlterField(
            model_name='locations',
            name='active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='city',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='field',
            field=models.CharField(max_length=36, null=True),
        ),
    ]
