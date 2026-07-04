from currencies.models import Currency
from rates.models import MarketRate


class MarketService:

    @staticmethod
    def generate_market_snapshot():

        currencies = Currency.objects.filter(is_active=True)

        snapshot = []

        for currency in currencies:

            # simple controlled pricing logic (better than random chaos)
            base_buy = 1500  # temporary anchor (we will later replace with API)
            spread = 10

            buy = base_buy + spread
            sell = base_buy + spread + 5

            snapshot.append(
                MarketRate(
                    currency=currency,
                    buy_rate=buy,
                    sell_rate=sell,
                    source="engine_v1"
                )
            )

        MarketRate.objects.bulk_create(snapshot)