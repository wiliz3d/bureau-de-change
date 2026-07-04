from django.urls import path

from .views import latest_rates

urlpatterns = [

    path(
        "rates/",
        latest_rates,
        name="api-rates",
    ),

]