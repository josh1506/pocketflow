from django.urls import path

from .views import ExpensesListView, ExpensesCreateView, ExpensesDetailView, ExpensesUpdateView

app_name = "expenses"

urlpatterns = [
    path('', ExpensesListView.as_view(), name='list'),
    path('create/', ExpensesCreateView.as_view(), name='create'),
    path('details/<str:expense_id>/', ExpensesDetailView.as_view(), name='details'),
    path('update/<str:expense_id>/', ExpensesUpdateView.as_view(), name='update'),
]
