from rest_framework.decorators import api_view
from rest_framework.response import Response

from rates.services.rate_service import RateService


@api_view(["GET"])
def latest_rates(request):

    rates = RateService.latest_rates()

    data = []

    for rate in rates:

        data.append({

            "company": rate.company.name,

            "currency": rate.currency.code,

            "buy": rate.buy_rate,

            "sell": rate.sell_rate,

            "updated": rate.updated_at,

        })

    return Response(data)