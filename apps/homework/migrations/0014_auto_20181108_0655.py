# Generated by Django 2.1.1 on 2018-11-08 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0013_auto_20181108_0650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criteriaanswer',
            name='submission',
        ),
        migrations.AddField(
            model_name='criteriaanswer',
            name='grade',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='criteria_answers', to='homework.Grade'),
        ),
    ]
