# Generated by Django 2.0 on 2021-12-19 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0004_auto_20211219_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='census',
            name='voter_ids',
        ),
    ]