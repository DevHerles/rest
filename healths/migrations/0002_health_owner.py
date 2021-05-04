# Generated by Django 3.2 on 2021-05-04 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('healths', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='health',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='healths', to=settings.AUTH_USER_MODEL),
        ),
    ]
