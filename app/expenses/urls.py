from django.urls import path

from .views import ExpensesListView

app_name = "expenses"

urlpatterns = [
    path('', ExpensesListView.as_view(), name='expenses_list'),
]
