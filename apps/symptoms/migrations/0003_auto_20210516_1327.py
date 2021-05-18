# Generated by Django 3.1.7 on 2021-05-16 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_remove_partner_healths'),
        ('symptoms', '0002_historicalsymptom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalsymptom',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='symptom',
            name='owner',
        ),
        migrations.AddField(
            model_name='historicalsymptom',
            name='partner_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='partners.partner'),
        ),
        migrations.AddField(
            model_name='symptom',
            name='partner_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='symptoms', to='partners.partner'),
        ),
    ]
