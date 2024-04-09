# Generated by Django 5.0.4 on 2024-04-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainform', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainform',
            old_name='name',
            new_name='project_name',
        ),
        migrations.AddField(
            model_name='mainform',
            name='area',
            field=models.CharField(choices=[('Indutry', 'Indutry'), ('Agriculture', 'Agriculture'), ('Tourism', 'Tourism')], default='', max_length=25),
            preserve_default=False,
        ),
    ]
