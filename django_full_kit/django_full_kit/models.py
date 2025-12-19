from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import auth,utils

class PhoneNumberField(models.CharField):
    """
    Custom Django model field for validating international phone numbers in E.164 format.
    Usage: like models.EmailField
    """
    default_validators = [
        auth.phone_number_validator
    ]

    description = "International phone number"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 16)
        super().__init__(*args, **kwargs)


class VideoField(models.FileField):
    """
    Custom Django model field for video
    Usage: like models.EmailField
    """
    default_validators = [
        utils.video_validator
    ]
    description = "support video number"