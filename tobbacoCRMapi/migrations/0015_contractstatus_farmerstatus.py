# Generated by Django 4.2.5 on 2023-09-24 18:02

import uuid

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tobbacoCRMapi', '0014_rename_emailaddress_contact_email_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False,
                 primary_key=True, serialize=False, unique=True)),
                ('color_codes', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(
                    default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='FarmerStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False,
                 primary_key=True, serialize=False, unique=True)),
                ('color_codes', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(
                    default=django.utils.timezone.now)),
            ],
        ),
    ]