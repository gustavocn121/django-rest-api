# Generated by Django 3.2.9 on 2021-11-20 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seazone_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seazone_api.calendar_date', verbose_name='assignment_date'),
        ),
    ]
