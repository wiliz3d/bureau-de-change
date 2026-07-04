import uuid

from django.conf import settings
from django.db import models

from companies.models import Company
from currencies.models import Currency


class CompanyRate(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="rates",
    )

    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name="company_rates",
    )

    buy_rate = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    sell_rate = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        unique_together = ("company", "currency")
        ordering = ["company", "currency"]

    def __str__(self):
        return f"{self.company} - {self.currency.code}"


class RateHistory(models.Model):
    company_rate = models.ForeignKey(
        CompanyRate,
        on_delete=models.CASCADE,
        related_name="history",
    )

    old_buy_rate = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    old_sell_rate = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    new_buy_rate = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    new_sell_rate = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    changed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.company_rate}"