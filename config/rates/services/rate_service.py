from rates.models import CompanyRate


class RateService:

    @staticmethod
    def company_rates(company):

        return (

            CompanyRate.objects

            .filter(company=company)

            .select_related(

                "currency",

            )

            .order_by("-updated_at")

        )

    @staticmethod
    def latest_rates():

        return CompanyRate.objects.select_related(

            "company",

            "currency",

        )