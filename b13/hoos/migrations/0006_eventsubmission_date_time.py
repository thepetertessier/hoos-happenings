# Generated by Django 4.2.7 on 2023-11-22 01:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoos', '0005_alter_eventsubmission_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsubmission',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 21, 20, 16, 51, 478501)),
        ),
    ]
