# Generated by Django 4.2.5 on 2023-09-25 19:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tobbacoCRMapi", "0021_files_images"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="images",
            name="name",
        ),
    ]
