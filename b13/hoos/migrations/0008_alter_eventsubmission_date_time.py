# Generated by Django 4.2.7 on 2023-11-22 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoos', '0007_alter_eventsubmission_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsubmission',
            name='date_time',
            field=models.DateTimeField(default=None),
        ),
    ]