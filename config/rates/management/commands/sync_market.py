from django.core.management.base import BaseCommand
from rates.services.market_service import MarketService
from rates.models import MarketRate


class Command(BaseCommand):

    help = "Generate market snapshot"

    def handle(self, *args, **kwargs):

        # optional cleanup so data doesn't stack forever
        MarketRate.objects.all().delete()

        MarketService.generate_market_snapshot()

        self.stdout.write(self.style.SUCCESS("Market snapshot generated"))