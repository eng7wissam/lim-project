# Generated by Django 5.0.4 on 2024-04-13 17:28

import mainform.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainform', '0011_mainform_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainform',
            name='image',
            field=models.ImageField(upload_to=mainform.models.image_upload),
        ),
    ]
