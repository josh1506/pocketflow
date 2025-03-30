from django import forms

from .models import Income


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = [
            "title",
            "amount",
            "category",
            "date",
            "description",
        ]
