from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from companies.services.company_service import get_user_company
from .forms import CompanyRateForm
from .models import CompanyRate


@login_required
def rate_list(request):

    company = get_user_company(request.user)

    rates = (
        CompanyRate.objects
        .filter(company=company)
        .select_related("currency")
        .order_by("-updated_at")
    )

    return render(
        request,
        "rates/rate_list.html",
        {
            "rates": rates,
        },
    )


@login_required
def add_rate(request):

    company = get_user_company(request.user)

    form = CompanyRateForm(request.POST or None)

    if form.is_valid():

        rate = form.save(commit=False)

        rate.company = company
        rate.updated_by = request.user

        rate.save()

        return redirect("rate-list")

    return render(
        request,
        "rates/add_rate.html",
        {
            "form": form,
        },
    )