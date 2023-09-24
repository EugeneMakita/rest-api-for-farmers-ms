from django.db import models
from django.contrib.auth.models import User
import uuid

class Farmer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    growers_number = models.CharField(max_length=50, unique=True)
    total_land = models.FloatField(default=0)
    address = models.TextField()
    CATEGORY_CHOICES = [
            ('a1', 'a1'),
            ('a2', 'a2')
        ]
    land_category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='a1')
    STATUS_OF_FARMER = [
            ('active', 'active'), 
            ('pending', 'pending'),
            ('contracted', 'contracted'),
            ('completed', 'completed'),
            ('inactive', 'inactive'),
            ('terminated', 'terminated'),
    ]
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='pending')

class SeasonNames(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    color_codes = models.CharField(max_length=8)
    name = models.CharField(max_length=50, unique=True)

class Season(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='seasons', null=True)
    growers_number = models.CharField(max_length=50, unique=True)
    total_land_grown = models.FloatField(default=0)
    year = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        unique_together = ('farmer', 'year')

class Contract(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

class Bale(models.Model):
    LEAF_POSITION = [
            ('L','Lugs'), 
            ('C','Cutters'), 
            ('B','Binds'), 
            ('F','Filters'), 
            ('S','Spreads'), 
    ]

    QUALITY_OF_BALE = [
            ('L','Lugs'), 
            ('C','Cutters'), 
            ('B','Binds'), 
            ('F','Filters'), 
            ('S','Spreads'), 
    ]

    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    #farmer_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    weight = models.FloatField()  # e.g., in kilograms
    price_per_kilogram = models.FloatField()  # e.g., in kilograms
    leaf_position = models.CharField(max_length=20, choices=LEAF_POSITION)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='bales', null=True)
    quality_of_bales = models.CharField(max_length=20, choices=QUALITY_OF_BALE)
