# Generated by Django 2.1.1 on 2019-11-26 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0050_auto_20191126_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='definition',
            old_name='max_submisions_per_student',
            new_name='max_submissions_per_student',
        ),
    ]
