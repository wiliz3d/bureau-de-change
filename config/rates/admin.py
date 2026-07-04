from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import CompanyRate, RateHistory


@admin.register(CompanyRate)
class CompanyRateAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "currency",
        "buy_rate",
        "sell_rate",
        "updated_at",
    )

    list_filter = (
        "company",
        "currency",
    )

    search_fields = (
        "company__name",
        "currency__code",
    )


@admin.register(RateHistory)
class RateHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "company_rate",
        "old_buy_rate",
        "new_buy_rate",
        "created_at",
    )

    readonly_fields = (
        "created_at",
    )