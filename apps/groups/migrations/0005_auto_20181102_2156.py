# Generated by Django 2.1.1 on 2018-11-02 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20181102_2141'),
        ('klasses', '0010_auto_20181018_1937'),
        ('groups', '0004_auto_20181102_2141'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InstructorGroup',
            new_name='Group',
        ),
        migrations.RenameModel(
            old_name='KlassTeam',
            new_name='Team',
        ),
    ]
