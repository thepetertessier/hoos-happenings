# Generated by Django 4.2.7 on 2023-12-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hoos", "0011_remove_eventsubmission_approved_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventsubmission",
            name="approval_status",
            field=models.CharField(
                choices=[
                    ("pending", "⏰ Pending"),
                    ("approved", "✅ Approved"),
                    ("rejected", "❌ Rejected"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]