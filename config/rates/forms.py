from django import forms

from .models import CompanyRate


class CompanyRateForm(forms.ModelForm):

    class Meta:
        model = CompanyRate

        fields = [
            "company",
            "currency",
            "buy_rate",
            "sell_rate",
        ]

        widgets = {
            "company": forms.Select(attrs={"class": "form-select"}),

            "currency": forms.Select(attrs={"class": "form-select"}),

            "buy_rate": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
            }),

            "sell_rate": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
            }),
        }