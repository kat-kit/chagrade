# Generated by Django 2.1.11 on 2019-12-11 00:31

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0050_auto_20191128_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='definition',
            name='force_github',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='is_direct_upload',
            field=models.BooleanField(default=False),
        ),
    ]
