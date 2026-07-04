from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class UserRole(models.TextChoices):
    PLATFORM_OWNER = "PLATFORM_OWNER", "Platform Owner"
    COMPANY_ADMIN = "COMPANY_ADMIN", "Company Admin"
    RATE_EDITOR = "RATE_EDITOR", "Rate Editor"
    VIEWER = "VIEWER", "Viewer"


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True
    )

    email = models.EmailField(
        unique=True
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    role = models.CharField(
        max_length=30,
        choices=UserRole.choices,
        default=UserRole.VIEWER
    )

    objects = CustomUserManager()

    # REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email