# Generated by Django 5.0.4 on 2024-05-16 17:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0023_rename_applicants_investors'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='appForm',
            new_name='Applicants',
        ),
    ]
