# Generated by Django 5.0.4 on 2024-04-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainform', '0010_mainform_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainform',
            name='image',
            field=models.ImageField(default='', upload_to='frms/'),
            preserve_default=False,
        ),
    ]
