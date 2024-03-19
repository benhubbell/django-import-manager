import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


def get_current_datetime_utc():
    print(timezone.now())
    return timezone.now()


class SignUpKey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20)
    salt = models.CharField(max_length=500)
    hashed_token = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=get_current_datetime_utc)
    duration_in_minutes = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1440)])
