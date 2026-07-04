from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from companies.services.company_service import get_user_company
from rates.models import MarketRate
from rates.services.analytics_service import RateAnalyticsService
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

    search = request.GET.get("search")

    if search:
        rates = rates.filter(currency__code__icontains=search)

    paginator = Paginator(rates, 10)
    page = request.GET.get("page")
    rates = paginator.get_page(page)

    # 🔥 NEW: market comparison data
    comparison = RateAnalyticsService.compare_rates(company)

    return render(
        request,
        "rates/rate_list.html",
        {
            "rates": rates,
            "comparison": comparison,
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


@login_required
def edit_rate(request, pk):

    company = get_user_company(request.user)

    rate = get_object_or_404(

        CompanyRate,

        pk=pk,

        company=company,

    )

    form = CompanyRateForm(

        request.POST or None,

        instance=rate,

    )

    if form.is_valid():

        rate = form.save(commit=False)

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


@login_required
def delete_rate(request, pk):

    company = get_user_company(request.user)

    rate = get_object_or_404(

        CompanyRate,

        pk=pk,

        company=company,

    )

    rate.delete()

    return redirect("rate-list")