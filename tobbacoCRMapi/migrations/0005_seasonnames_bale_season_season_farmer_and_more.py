# Generated by Django 4.2.5 on 2023-09-24 02:06

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tobbacoCRMapi', '0004_farmer_land_category_farmer_total_land_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonNames',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False,
                 primary_key=True, serialize=False, unique=True)),
                ('color_codes', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='bale',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='bales', to='tobbacoCRMapi.season'),
        ),
        migrations.AddField(
            model_name='season',
            name='farmer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='seasons', to='tobbacoCRMapi.farmer'),
        ),
        migrations.AddField(
            model_name='season',
            name='growers_number',
            field=models.CharField(default=101, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='season',
            name='year',
            field=models.PositiveIntegerField(default=2023),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='season',
            unique_together={('farmer', 'year')},
        ),
    ]