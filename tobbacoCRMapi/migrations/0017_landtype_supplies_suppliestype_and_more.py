# Generated by Django 4.2.5 on 2023-09-24 18:20

import uuid

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tobbacoCRMapi", "0016_farmer"),
    ]

    operations = [
        migrations.CreateModel(
            name="LandType",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("color_codes", models.CharField(max_length=8)),
                ("name", models.CharField(max_length=50, unique=True)),
                ("created", models.DateTimeField(
                    default=django.utils.timezone.now)),
                ("modified", models.DateTimeField(
                    default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Supplies",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("amount", models.IntegerField(default=0)),
                ("created", models.DateTimeField(
                    default=django.utils.timezone.now)),
                ("modified", models.DateTimeField(
                    default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="SuppliesType",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("color_codes", models.CharField(max_length=8)),
                ("name", models.CharField(max_length=50, unique=True)),
                ("created", models.DateTimeField(
                    default=django.utils.timezone.now)),
                ("modified", models.DateTimeField(
                    default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameField(
            model_name="farmer",
            old_name="address",
            new_name="address_line_of_farm",
        ),
        migrations.RemoveField(
            model_name="farmer",
            name="user",
        ),
        migrations.AddField(
            model_name="farmer",
            name="address_line_two_of_farm",
            field=models.TextField(default=str),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="farmer",
            name="city_of_farm",
            field=models.TextField(default=str),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="farmer",
            name="country_of_farm",
            field=models.TextField(default=str),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="farmer",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="farmer",
            name="full_name",
            field=models.CharField(default=str, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="farmer",
            name="last_name",
            field=models.CharField(default=str, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="farmer",
            name="national_id",
            field=models.CharField(default=str, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="farmer",
            name="province_of_farm",
            field=models.TextField(default=str),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="farmer",
            name="sex",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                default=str,
                max_length=10,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="farmer",
            name="title",
            field=models.CharField(
                choices=[("Mr", "Mr"), ("Mrs", "Mrs"),
                         ("Ms", "Ms"), ("Dr", "Doctor")],
                default=str,
                max_length=10,
            ),
            preserve_default=False,
        ),
    ]
