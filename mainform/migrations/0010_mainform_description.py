# Generated by Django 5.0.4 on 2024-04-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainform', '0009_alter_type_activity_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainform',
            name='description',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
    ]