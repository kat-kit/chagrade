# Generated by Django 2.1.1 on 2019-01-31 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klasses', '0011_auto_20181127_2226'),
        ('profiles', '0008_auto_20190125_0413'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studentmembership',
            unique_together={('user', 'klass')},
        ),
    ]
