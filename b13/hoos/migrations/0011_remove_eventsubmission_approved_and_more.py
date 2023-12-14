# Generated by Django 4.2.7 on 2023-11-24 23:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hoos", "0010_tag_remove_eventsubmission_tag_eventsubmission_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eventsubmission",
            name="approved",
        ),
        migrations.AddField(
            model_name="eventsubmission",
            name="approval_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("approved", "Approved"),
                    ("rejected", "Rejected"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]
