# Generated by Django 2.1.1 on 2018-11-08 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0017_auto_20181108_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='overall_grade',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
