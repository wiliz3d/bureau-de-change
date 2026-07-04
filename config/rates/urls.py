from django.urls import path

from .views import (
    add_rate,
    delete_rate,
    edit_rate,
    rate_list,
)

urlpatterns = [

    path("", rate_list, name="rate-list"),

    path("add/", add_rate, name="add-rate"),

    path(
        "edit/<uuid:pk>/",
        edit_rate,
        name="edit-rate",
    ),

    path(
        "delete/<uuid:pk>/",
        delete_rate,
        name="delete-rate",
    ),

]