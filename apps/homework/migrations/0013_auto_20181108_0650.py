# Generated by Django 2.1.1 on 2018-11-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0012_auto_20181108_0444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criteriaanswer',
            name='text',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='score',
        ),
        migrations.AddField(
            model_name='criteriaanswer',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
