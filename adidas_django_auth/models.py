import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    DEVELOPER = 'developer'
    ADMIN = 'admin'
    CUSTOMER = 'customer'
    ROLE_CHOICES = [
        (DEVELOPER, 'developer'),
        (ADMIN, 'admin'),
        (CUSTOMER, 'customer')
    ]
    FEMALE = 'female'
    MALE = 'male'
    OTHER = 'other'
    GENDER_CHOICES = [
        (FEMALE, 'female'),
        (MALE, 'male'),
        (OTHER, 'other')
    ]

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    role = models.CharField(max_length=9, choices=ROLE_CHOICES,
                            null=True, blank=True, default=CUSTOMER)
    dob = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)

    class Meta:
        db_table = "user"
