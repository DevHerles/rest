# Generated by Django 3.1.7 on 2021-05-16 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healths', '0002_historicalhealth'),
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='healths',
            field=models.ManyToManyField(blank=True, to='healths.Health'),
        ),
    ]
