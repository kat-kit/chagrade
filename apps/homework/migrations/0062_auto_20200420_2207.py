# Generated by Django 2.2.10 on 2020-04-20 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0061_auto_20200326_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteriaanswer',
            name='score',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='grade',
            name='jupyter_notebook_grade',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='grade',
            name='overall_grade',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=6),
        ),
    ]
