# Generated by Django 5.0.4 on 2024-04-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainform', '0005_mainform_person'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainform',
            old_name='phone',
            new_name='phone1',
        ),
        migrations.AddField(
            model_name='mainform',
            name='nation',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainform',
            name='passport',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainform',
            name='phone2',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainform',
            name='possition',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
