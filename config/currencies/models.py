import uuid

from django.db import models


class Currency(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    code = models.CharField(
        max_length=3,
        unique=True,
    )

    name = models.CharField(
        max_length=100,
    )

    symbol = models.CharField(
        max_length=10,
    )

    country = models.CharField(
        max_length=100,
    )

    country_code = models.CharField(
        max_length=2,
        default="NG",
        help_text="ISO Country Code (US, GB, NG...)",
    )

    decimal_places = models.PositiveSmallIntegerField(
        default=2,
    )

    flag = models.ImageField(
        upload_to="currency_flags/",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["code"]
        verbose_name_plural = "Currencies"

    def __str__(self):
        return f"{self.code} - {self.name}"