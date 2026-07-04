from decimal import Decimal

from rates.models import CompanyRate


class ConverterService:

    @staticmethod
    def convert(company, currency, amount, transaction_type):

        rate = CompanyRate.objects.filter(
            company=company,
            currency=currency,
        ).first()

        if not rate:
            return None

        if transaction_type == "BUY":

            exchange_rate = rate.buy_rate

        else:

            exchange_rate = rate.sell_rate

        result = Decimal(amount) * exchange_rate

        return {

            "rate": exchange_rate,

            "result": result,

        }