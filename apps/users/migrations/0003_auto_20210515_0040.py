# Generated by Django 3.1.7 on 2021-05-15 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210515_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicaluser',
            old_name='photo',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='photo',
            new_name='image',
        ),
    ]
