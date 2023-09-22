# Generated by Django 4.2.5 on 2023-09-22 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tobbacoCRMapi', '0003_remove_bale_uuid_remove_contract_uuid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='land_category',
            field=models.CharField(choices=[('a1', 'a1'), ('a2', 'a2')], default='a1', max_length=3),
        ),
        migrations.AddField(
            model_name='farmer',
            name='total_land',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='season',
            name='total_land_grown',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='category',
            field=models.CharField(choices=[('a1', 'a1'), ('a2', 'a2')], default='pending', max_length=3),
        ),
    ]
