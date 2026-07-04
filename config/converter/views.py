from django.shortcuts import render

from .forms import ConverterForm
from .services.converter_service import ConverterService


def converter(request):

    form = ConverterForm(request.POST or None)

    result = None

    if request.method == "POST" and form.is_valid():

        data = ConverterService.convert(

            company=form.cleaned_data["company"],

            currency=form.cleaned_data["currency"],

            amount=form.cleaned_data["amount"],

            transaction_type=form.cleaned_data["transaction_type"],

        )

        result = data

    return render(

        request,

        "converter/converter.html",

        {

            "form": form,

            "result": result,

        },

    )