from django.urls import path

from .views import IncomeListView

app_name = "income"

urlpatterns = [
    path('', IncomeListView.as_view(), name='income_list'),
]
