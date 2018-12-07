# Generated by Django 2.1.1 on 2018-10-25 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0007_auto_20181024_0711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='klass',
        ),
        migrations.AddField(
            model_name='submission',
            name='definition',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='homework_submissions', to='homework.Definition'),
        ),
    ]
