# Generated by Django 3.0.6 on 2020-05-16 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200516_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='video_file',
            new_name='file',
        ),
    ]
