import uuid

from django.db import models
from django.utils import timezone


class Farmer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    TITLE_CHOICES = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Dr', 'Doctor'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    growers_number = models.CharField(max_length=50, unique=True)
    national_id = models.CharField(max_length=50,)
    full_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    total_land = models.FloatField(default=0)
    address_line_of_farm = models.TextField()
    address_line_two_of_farm = models.TextField()
    province_of_farm = models.TextField()
    city_of_farm = models.TextField()
    country_of_farm = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
