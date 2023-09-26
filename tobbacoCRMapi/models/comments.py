import uuid

from django.db import models
from django.utils import timezone


class Comments(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    is_deleted = models.BooleanField(default=False)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
