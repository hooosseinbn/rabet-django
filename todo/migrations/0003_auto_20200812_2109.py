# Generated by Django 3.0 on 2020-08-12 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200131_0131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='memo',
            new_name='skill',
        ),
    ]
