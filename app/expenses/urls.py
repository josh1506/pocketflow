from django.urls import path

from .views import ExpensesListView, ExpensesCreateView

app_name = "expenses"

urlpatterns = [
    path('', ExpensesListView.as_view(), name='list'),
    path('create/', ExpensesCreateView.as_view(), name='create'),
]
