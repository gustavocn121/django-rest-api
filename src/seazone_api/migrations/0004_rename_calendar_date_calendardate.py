# Generated by Django 3.2.9 on 2021-11-20 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seazone_api', '0003_alter_assignment_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='calendar_date',
            new_name='CalendarDate',
        ),
    ]