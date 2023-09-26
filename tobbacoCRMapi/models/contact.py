import uuid

from django.db import models
from django.utils import timezone


class Contact(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    post_code = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
