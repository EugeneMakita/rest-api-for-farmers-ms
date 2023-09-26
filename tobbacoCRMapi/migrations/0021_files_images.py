# Generated by Django 4.2.5 on 2023-09-25 00:25

import uuid

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tobbacoCRMapi", "0020_comments"),
    ]

    operations = [
        migrations.CreateModel(
            name="Files",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("path", models.CharField(blank=True, max_length=255, null=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("modified", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Images",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("thumbnail", models.CharField(blank=True, max_length=255, null=True)),
                ("small", models.CharField(blank=True, max_length=255, null=True)),
                ("large", models.CharField(blank=True, max_length=255, null=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("modified", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
