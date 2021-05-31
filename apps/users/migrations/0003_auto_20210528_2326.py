# Generated by Django 3.1.7 on 2021-05-29 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_auto_20210526_0132'),
        ('users', '0002_auto_20210527_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='settings',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='settings.setting'),
        ),
        migrations.AddField(
            model_name='user',
            name='settings',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='settings.setting'),
            preserve_default=False,
        ),
    ]
