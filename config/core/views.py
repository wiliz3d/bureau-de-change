from django.shortcuts import render

from currencies.models import Currency
from rates.models import CompanyRate


def home(request):

    currencies = Currency.objects.filter(is_active=True)

    latest_rates = (
        CompanyRate.objects
        .select_related("company", "currency")
        .order_by("currency__code")
    )

    context = {
        "currencies": currencies,
        "latest_rates": latest_rates,
    }

    return render(request, "home.html", context)