from rates.models import MarketRate
from companies.models import Company
from rates.models import CompanyRate


class RateAnalyticsService:

    @staticmethod
    def compare_rates(company):

        latest_market = (
            MarketRate.objects
            .select_related("currency")
            .order_by("currency", "-created_at")
        )

        results = []

        for market in latest_market:

            try:
                company_rate = CompanyRate.objects.get(
                    company=company,
                    currency=market.currency
                )

                spread_buy = company_rate.buy_rate - market.buy_rate
                spread_sell = company_rate.sell_rate - market.sell_rate

                results.append({
                    "currency": market.currency.code,
                    "market_buy": market.buy_rate,
                    "market_sell": market.sell_rate,
                    "company_buy": company_rate.buy_rate,
                    "company_sell": company_rate.sell_rate,
                    "spread_buy": spread_buy,
                    "spread_sell": spread_sell,
                })

            except CompanyRate.DoesNotExist:
                continue

        return results