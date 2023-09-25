from django.db import models
import uuid
from django.utils import timezone

class Images(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thumbnail = models.CharField(max_length=255, null=True, blank=True)
    small = models.CharField(max_length=255, null=True, blank=True)
    large = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)