from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "symbol",
        "country",
        "is_active",
    )

    search_fields = (
        "code",
        "name",
        "country",
    )

    list_filter = (
        "is_active",
        "country",
    )