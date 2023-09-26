# Generated by Django 4.2.5 on 2023-09-22 00:50

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Bale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4,
                                     editable=False, unique=True),
                ),
                ("weight", models.FloatField()),
                ("price_per_kilogram", models.FloatField()),
                (
                    "leaf_position",
                    models.CharField(
                        choices=[
                            ("L", "Lugs"),
                            ("C", "Cutters"),
                            ("B", "Binds"),
                            ("F", "Filters"),
                            ("S", "Spreads"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "quality_of_bales",
                    models.CharField(
                        choices=[
                            ("L", "Lugs"),
                            ("C", "Cutters"),
                            ("B", "Binds"),
                            ("F", "Filters"),
                            ("S", "Spreads"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4,
                                     editable=False, unique=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Season",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4,
                                     editable=False, unique=True),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Farmer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("growers_number", models.CharField(max_length=50, unique=True)),
                ("address", models.TextField()),
                (
                    "category",
                    models.CharField(
                        choices=[("A1", "A1"), ("A2", "A2")], max_length=3
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
