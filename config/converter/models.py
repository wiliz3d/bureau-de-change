import uuid

from django.db import models

from companies.models import Company
from currencies.models import Currency


class ConversionHistory(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    from_currency = models.ForeignKey(
        Currency,
        related_name="from_currency",
        on_delete=models.CASCADE,
    )

    to_currency = models.ForeignKey(
        Currency,
        related_name="to_currency",
        on_delete=models.CASCADE,
    )

    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )

    rate = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )

    result = models.DecimalField(
        max_digits=20,
        decimal_places=2,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.amount} {self.from_currency.code}"