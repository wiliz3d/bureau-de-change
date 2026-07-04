from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Company, CompanyMembership


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "country",
        "is_active",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    search_fields = (
        "name",
        "email",
    )

    list_filter = (
        "country",
        "is_active",
    )


@admin.register(CompanyMembership)
class CompanyMembershipAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "user",
        "role",
    )

    list_filter = (
        "role",
    )