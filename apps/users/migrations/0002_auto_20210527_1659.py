# Generated by Django 3.1.7 on 2021-05-27 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='groups',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='auth.group'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
            preserve_default=False,
        ),
    ]
