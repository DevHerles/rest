# Generated by Django 3.1.7 on 2021-05-30 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210529_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaluser',
            name='settings',
        ),
        migrations.RemoveField(
            model_name='user',
            name='settings',
        ),
    ]
