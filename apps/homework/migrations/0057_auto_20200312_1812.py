# Generated by Django 2.2.10 on 2020-03-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0056_grade_needs_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='needs_review',
            field=models.BooleanField(default=True),
        ),
    ]
