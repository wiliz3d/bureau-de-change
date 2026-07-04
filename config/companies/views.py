from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from companies.services.company_service import get_user_company


@login_required
def company_list(request):

    company = get_user_company(request.user)

    context = {
        "company": company,
    }

    return render(
        request,
        "companies/company_list.html",
        context,
    )