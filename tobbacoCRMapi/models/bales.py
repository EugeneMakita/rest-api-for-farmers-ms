import uuid

from django.db import models
from django.utils import timezone


class Bales(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    weight = models.FloatField()
    price_per_kilogram = models.FloatField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
