# Generated by Django 5.0.4 on 2024-04-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainform', '0015_get_opportunnity'),
    ]

    operations = [
        migrations.AddField(
            model_name='get_opportunnity',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
