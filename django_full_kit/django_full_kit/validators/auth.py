from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(
    regex=r'^\+[1-9]\d{1,14}$',
    message="Phone number must be entered in E.164 format (e.g. +989123456789)."
)