import uuid

from django.db import models
from django.utils import timezone


class FarmerStatus(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    color_codes = models.CharField(max_length=8)
    name = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
