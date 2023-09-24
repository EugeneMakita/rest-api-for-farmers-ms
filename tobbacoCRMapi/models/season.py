import uuid

from django.db import models
from django.utils import timezone


class Season(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    growers_number = models.CharField(max_length=50, unique=True)
    total_land_grown = models.FloatField(default=0)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
