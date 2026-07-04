from django import forms

from companies.models import Company
from currencies.models import Currency


class ConverterForm(forms.Form):

    company = forms.ModelChoiceField(

        queryset=Company.objects.filter(
            is_active=True
        ),

        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )

    currency = forms.ModelChoiceField(

        queryset=Currency.objects.filter(
            is_active=True
        ),

        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )

    amount = forms.DecimalField(

        decimal_places=2,

        max_digits=15,

        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Amount",
            }
        ),
    )

    transaction_type = forms.ChoiceField(

        choices=[
            ("BUY", "Buy"),
            ("SELL", "Sell"),
        ],

        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )