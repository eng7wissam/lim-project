# Generated by Django 5.0.4 on 2024-04-14 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainform', '0013_mainform_address_mainform_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainform',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
