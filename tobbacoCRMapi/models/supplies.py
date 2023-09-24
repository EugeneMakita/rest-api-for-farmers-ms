import uuid

from django.db import models
from django.utils import timezone


class Supplies(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    amount = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
