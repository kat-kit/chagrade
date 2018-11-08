# Generated by Django 2.1.1 on 2018-11-08 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0011_auto_20181106_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='method_description',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='method_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='project_url',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='publication_url',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
