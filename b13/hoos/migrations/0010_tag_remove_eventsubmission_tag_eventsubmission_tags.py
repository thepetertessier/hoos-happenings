# Generated by Django 4.2.7 on 2023-11-22 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoos', '0009_alter_eventsubmission_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='eventsubmission',
            name='tag',
        ),
        migrations.AddField(
            model_name='eventsubmission',
            name='tags',
            field=models.ManyToManyField(to='hoos.tag'),
        ),
    ]