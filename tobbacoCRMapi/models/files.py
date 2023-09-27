import uuid

from django.db import models
from django.utils import timezone

from ..services.files_service import FileService


class Files(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    path = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def delete(self, *args, **kwargs):
        FileService.delete_file(self)
        super(Files, self).delete(*args, **kwargs)
