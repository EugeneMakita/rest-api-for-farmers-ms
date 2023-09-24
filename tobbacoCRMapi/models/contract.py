import uuid

from django.db import models
from django.utils import timezone


class Contract(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
