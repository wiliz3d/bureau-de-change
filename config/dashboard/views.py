from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from companies.services.company_service import get_user_company
from currencies.models import Currency
from rates.models import CompanyRate


@login_required
def dashboard(request):

    company = get_user_company(request.user)

    rates = CompanyRate.objects.filter(
        company=company
    )

    context = {

        "company": company,

        "total_rates": rates.count(),

        "total_currencies": Currency.objects.count(),

        "latest_rates": rates.order_by("-updated_at")[:5],

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )