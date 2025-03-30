from django import forms

from .models import Expenses


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = (
            "title",
            "amount",
            "category",
            "description",
        )
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sm",
                "placeholder": "Enter title",
            }),
            "amount": forms.NumberInput(attrs={
                "class": "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sm",
                "placeholder": "Enter amount",
            }),
            "category": forms.Select(attrs={
                "class": "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sm",
            }),
            "description": forms.Textarea(attrs={
                "class": "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sm",
                "placeholder": "Enter description",
                "rows": 3,
            }),
        }
