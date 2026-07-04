from django.urls import path

from .views import add_rate, rate_list

urlpatterns = [

    path(
        "",
        rate_list,
        name="rate-list",
    ),

    path(
        "add/",
        add_rate,
        name="add-rate",
    ),

]