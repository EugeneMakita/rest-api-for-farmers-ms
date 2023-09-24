import uuid

from django.db import models


class SeasonNames(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    color_codes = models.CharField(max_length=8)
    name = models.CharField(max_length=50, unique=True)
