# Generated by Django 2.1.1 on 2019-11-28 18:58

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0049_auto_20191118_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissiontracker',
            name='stored_logs',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        )
    ]
