from django.core.management.base import BaseCommand

from currencies.models import Currency


class Command(BaseCommand):

    help = "Seed the application database."

    def handle(self, *args, **kwargs):

        currencies = [

            ("USD","US Dollar","$","United States","US"),
            ("GBP","British Pound","£","United Kingdom","GB"),
            ("EUR","Euro","€","European Union","EU"),
            ("NGN","Nigerian Naira","₦","Nigeria","NG"),
            ("AED","UAE Dirham","د.إ","United Arab Emirates","AE"),
            ("CAD","Canadian Dollar","C$","Canada","CA"),
            ("JPY","Japanese Yen","¥","Japan","JP"),
            ("CHF","Swiss Franc","CHF","Switzerland","CH"),
            ("AUD","Australian Dollar","A$","Australia","AU"),
            ("CNY","Chinese Yuan","¥","China","CN"),
            ("GHS","Ghana Cedi","₵","Ghana","GH"),
            ("ZAR","South African Rand","R","South Africa","ZA"),

        ]

        for code, name, symbol, country, country_code in currencies:

            Currency.objects.update_or_create(

                code=code,

                defaults={

                    "name": name,

                    "symbol": symbol,

                    "country": country,

                    "country_code": country_code,

                }

            )

        self.stdout.write(

            self.style.SUCCESS(

                "Database seeded successfully."

            )

        )